Imports System
Imports System.IO
Imports Google
Imports GoogleDriveExplorer

Public Class Form1

    Dim rootDir = File_Integrity_Checker.My.Computer.FileSystem.CurrentDirectory()
    Dim userpath = rootDir + "\" + "Program Data\users.txt"
    Dim prevdir As String
    Dim watchlistpath = rootDir + "\" + "Program Data\watchlist.txt"
    Dim watchflag = False
    Dim FileList As New List(Of String)
    Dim logDir = rootDir + "\" + "Program Data\eventlog.txt"
    Dim watchdict As New Dictionary(Of String, String)
    Dim lendict As New Dictionary(Of Integer, String)
    Dim newwatchdict As New Dictionary(Of String, String)
    Dim Eventlist As New List(Of String)
    Dim SecCounter As Timer
    


    
    Private Sub Check_Changes()
        
    End Sub
    
    Private Sub expandwatchlist()
        Dim newdict As New Dictionary(Of String, String)
        For Each Path In watchdict.Keys
            Dim pathsplit = Path.Split("\").ToList
            Dim num = 0
            Dim str = pathsplit(0)
            If Not watchdict.ContainsKey(pathsplit(0) + "\") Then
                newdict.Add(str + "\", "P")
            End If
            While num < pathsplit.Count
                str = str + "\" + pathsplit(num)
                If Not watchdict.ContainsKey(str) Then
                    newdict.Add(str, "P")
                End If
                Dim len = str.Split("\").Count()
                If lendict.ContainsKey(len) Then
                    Dim tmp = lendict.Item(len)
                    lendict.Remove(len)
                    lendict.Add(len, tmp + "," + str)
                Else
                    lendict.Add(len, str)
                End If
                num = num + 1
            End While
        Next
        watchdict = newdict
        update_watchlistfile()
    End Sub
    '''Event Log Form:
    '''Path, DateModified, DateDetected
    '''
    Private Sub LoadEventLog()
        Dim f = File.ReadAllLines("EventLogPath")
        For Each line In f
            Eventlist.Add(line)
            Dim split1 = line.Split(",")
            Dim path = split1(0)
            Dim DateModified = split1(1)
            Dim DateDetected = split1(2)
            LogBox.Items.Add(DateDetected.ToString() + ":" + vbTab +
                            DateModified.ToString() + vbTab + path.ToString())
        Next
    End Sub


    '''data can be Path, DateModified, or DateDetected
    Public Function SortEventLog(data As String)
        If data = "Path" Then
            LogBox.Items.Clear()
            For Each line In Eventlist
                Dim split1 = line.Split(",")
                Dim path = split1(0)
                Dim DateModified = split1(1)
                Dim DateDetected = split1(2)
                If LogBox.Items.Count() = 0 Then
                    LogBox.Items.Add(path.ToString + ":" + vbTab +
                                            DateModified + vbTab + DateDetected)

                End If
            Next
        Else

        End If
        Return 1
    End Function

    Private Sub build_dictionaries()
        Try
            Dim f = File.ReadAllLines(watchlistpath)
            For Each line In f
                watchdict.Add(line.Split(",")(0), line.Split("\")(1))
                Dim leng = line.Split(",")(0).Split("\").Length()
                If lendict.Keys.Contains(leng) Then
                    Dim temp = lendict.Item(leng)
                    lendict.Remove(leng)
                    lendict.Add(leng, temp + "," + line.Split(",")(0))
                Else
                    lendict.Add(line.Split(",")(0).Split("\").Length(), line.Split("\")(0))
                End If
            Next
        Catch ex As Exception
            clean_watchfile()
            build_dictionaries()
        End Try
        Return
    End Sub

    Private Sub clean_watchfile()
        Dim outlist As New List(Of String)
        For Each line In File.ReadAllLines(watchlistpath())
            If Not outlist.Contains(line) Then
                outlist.Add(line)
            End If
        Next
        File.Delete(watchlistpath)
        Dim f1 = File.CreateText(watchlistpath)
        For Each line In outlist
            f1.WriteLine(line)
        Next
        f1.Close()
        Return
    End Sub

    ''' <summary>
    '''This function takes the path of an item and returns any children in the watchlist
    ''' </summary>
    ''' <param name="Parent"></param>
    ''' <remarks></remarks>
    Public Function isChildOf(Parent As String)
        Dim plen = Parent.Split("\").Length()
        Dim result As New List(Of String)
        For Each entry In lendict.Item(plen + 1).Split(",")
            If entry.ToString.Contains(Parent.ToString) Then
                result.Add(entry)
            End If
        Next
        Return result
    End Function

    Public Function isParentOf(Child As String)
        Dim clen = Child.Split("\").Length()
        Dim result As New List(Of String)
        For Each entry In lendict.Item(clen - 1).Split(",")
            If Child.Contains(entry) Then
                result.Add(entry)
            End If
        Next
        Return result
    End Function

    Private Sub Check_files()
        If Not My.Computer.FileSystem.DirectoryExists(rootDir + "\Program Data") Then
            My.Computer.FileSystem.CreateDirectory(rootDir + "\Program Data")
        End If
        If Not My.Computer.FileSystem.FileExists(watchlistpath) Then
            Dim fs As FileStream = File.Create(watchlistpath)
            fs.Close()
            watchflag = True
        End If
        If Not My.Computer.FileSystem.FileExists(userpath) Then
            Dim fs As FileStream = File.Create(userpath)
            fs.Close()
        End If
        If Not My.Computer.FileSystem.FileExists(logDir) Then
            Dim fs As FileStream = File.Create(logDir)
            fs.Close()
        End If
    End Sub
    
    Private Sub Clean_watchlist()
        For Each item In watchdict.Keys()
            For Each item2 In watchdict.Keys()
                If item = item2 Then
                    watchlist.Items.Remove(watchlist.Items.IndexOf(item))
                End If
            Next
        Next
    End Sub

    Private Sub Refresh_Watchlistbox()
        Try
            expandwatchlist()
            If watchpath.Text() = "" Then
                watchlist.Items.Clear()
                For Each path In lendict.Item(1).Split("\")
                    watchlist.Items.Add(path)
                Next
            Else
                Try
                    Dim children = isChildOf(watchpath.Text())
                    watchlist.Items.Clear()
                    watchlist.Items.Add("...")
                    For Each child In children
                        watchlist.Items.Add(child.ToString.Trim(watchpath.Text()))
                    Next
                Catch ex As Exception

                End Try
            End If
        Catch

        End Try
    End Sub

    Private Function update_watchlistfile()
        File.Delete(watchlistpath)
        Dim f = File.CreateText(watchlistpath)
        For Each item In watchdict.Keys()
            f.WriteLine(item, watchdict.Item(item))
        Next
        f.Close()
        Return 1
    End Function

    Private Sub Load_All_Files()
        Dim allDrives() As DriveInfo = DriveInfo.GetDrives()
        Dim d As DriveInfo
        For Each d In allDrives
            If d.IsReady = True Then
                For Each file1 In Directory.EnumerateFiles(d.ToString)
                    FileList.Add(file1)
                Next
            End If
        Next

    End Sub

    Private Sub SearchFiles()

    End Sub

    Private Sub Refresh_click(sender As Object, e As EventArgs) Handles Refresh.Click
        If Directory.Exists(pathbox.Text.ToString) Then
            FileExplorer.Items.Clear()
            If Not pathbox.Text.ToString.Length = 3 Then
                FileExplorer.Items.Add("...")
                For Each subdir In Directory.EnumerateDirectories(pathbox.Text.ToString)
                    FileExplorer.Items.Add(subdir)
                Next
                For Each file1 In Directory.EnumerateFiles(pathbox.Text.ToString)
                    FileExplorer.Items.Add(file1)
                Next
            End If
        ElseIf pathbox.Text.ToString.Contains("\") = False Then
            SearchFiles()
        Else
            MsgBox("Directory does not exsist. Check the path and try again.")
        End If
    End Sub

    Private Sub Load_Log()
        LogBox.Items.Clear()
        If File.Exists(LogDir) Then
            For Each line In File.ReadLines(LogDir)
                LogBox.Items.Add(line)
            Next
        Else
            File.Create(LogDir)
        End If
    End Sub

    Private Sub Clear_Log()
        LogBox.Items.Clear()
        File.Delete(LogDir)
        Load_Log()
    End Sub


    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Check_files()
        Me.Size = New Size(400, 200)
        draw_login_buttons()
        build_dictionaries()
    End Sub

    Private Sub draw_login_buttons()
        undraw_all()
        LocalSignin.Visible = True
        GoogleLoginButton.Visible = True
        CreateNewButton.Visible = True
    End Sub

    Private Sub undraw_all()
        LocalSignin.Visible = False
        GoogleLoginButton.Visible = False
        CreateNewButton.Visible = False
        usernamebox.Visible = False
        UsernameLabel.Visible = False
        Passwordbox.Visible = False
        passwordlabel.Visible = False
        LoginButton.Visible = False
        Create.Visible = False
        BackButton.Visible = False
        watchlist.Visible = False
        FileExplorer.Visible = False
        pathbox.Visible = False
        Button1.Visible = False
        Button2.Visible = False
        Refresh.Visible = False
        watchpath.Visible = False
        LogBox.Visible = False
        Label1.Visible = False
        Label2.Visible = False
        Label3.Visible = False

    End Sub

    Private Sub draw_login()
        undraw_all()
        usernamebox.Visible = True
        UsernameLabel.Visible = True
        Passwordbox.Visible = True
        passwordlabel.Visible = True
        LoginButton.Visible = True
        BackButton.Visible = True
    End Sub

    Private Sub LocalSignin_Click(sender As Object, e As EventArgs) Handles LocalSignin.Click
        draw_login()
    End Sub

    Private Sub GoogleLoginButton_Click(sender As Object, e As EventArgs) Handles GoogleLoginButton.Click
        draw_login()
        UsernameLabel.Text = "Google Email"
    End Sub

    Private Sub CreateNew_Click(sender As Object, e As EventArgs) Handles CreateNewButton.Click
        draw_login()
        LoginButton.Visible = False
        Create.Visible = True
    End Sub



    Private Sub Create_Click(sender As Object, e As EventArgs) Handles Create.Click
        Dim found As Boolean = False
        If Not usernamebox.Text = "" Or Passwordbox.Text = "" Then
            For Each line In System.IO.File.ReadLines(userpath)
                If line.Split("|")(0).ToString = usernamebox.Text() Then
                    found = True
                End If
            Next
            If found = True Then
                MsgBox("Username already exsists locally. Try logging in.")
            Else
                Using sw As StreamWriter = System.IO.File.AppendText(userpath)
                    sw.WriteLine(usernamebox.Text() + "|" + Passwordbox.Text())
                End Using
                undraw_all()
                draw_login()
                MsgBox("Account created. Login now.")
            End If
        Else
            MsgBox("Invalid Username or Password")
        End If
    End Sub

    Private Sub LoginButton_Click(sender As Object, e As EventArgs) Handles LoginButton.Click
        Dim flag = False
        For Each line In System.IO.File.ReadLines(userpath)
            If line.Split("|")(0) = usernamebox.Text() Then
                If line.Split("|")(1) = Passwordbox.Text() Then
                    flag = True
                End If
            End If
        Next
        If flag = True Then
            draw_main()
        End If
    End Sub

    Private Sub draw_main()
        undraw_all()
        Me.Size = New Size(800, 600)
        FileExplorer.Visible = True
        watchlist.Visible = True
        pathbox.Visible = True
        Button1.Visible = True
        Button2.Visible = True
        Refresh.Visible = True
        LogBox.Visible = True
        pathbox.Visible = True
        Label1.Visible = True
        Label2.Visible = True
        Label3.Visible = True
        load_explorer()
    End Sub

    Private Sub BackButton_Click(sender As Object, e As EventArgs) Handles BackButton.Click
        draw_login_buttons()
    End Sub

    Private Sub load_explorer()
        FileExplorer.Items.Clear()
        Dim allDrives() As DriveInfo = DriveInfo.GetDrives()
        Dim d As DriveInfo
        For Each d In allDrives
            If d.IsReady = True Then
                FileExplorer.Items.Add(d.Name.ToString())
            End If
        Next
    End Sub

    Private Sub FileExplorer_SelectedIndexChanged(sender As Object, e As EventArgs) Handles FileExplorer.DoubleClick
        If FileExplorer.SelectedItem.ToString = "..." Then
            Dim var = pathbox.Text.ToString.Remove(pathbox.Text.Length - 1, 1)
            Dim newdir = Directory.GetParent(pathbox.Text.Remove(pathbox.Text.Length - 1, 1))
            If var.Length < 3 Then
                pathbox.Text = ""
            Else
                pathbox.Text = newdir.ToString()
            End If
        ElseIf FileExplorer.SelectedItem.ToString.ToCharArray.Last() = "\" Then
            pathbox.Text = pathbox.Text + FileExplorer.SelectedItem.ToString()
        End If
    End Sub


    Private Sub pathbox_TextChanged() Handles pathbox.TextChanged
        If Directory.Exists(pathbox.Text) = True Then
            FileExplorer.Items.Clear()
            If Not pathbox.Text.Split("\").Length = 1 Then
                FileExplorer.Items.Add("...")
            End If
            For Each subdir In Directory.EnumerateDirectories(pathbox.Text())
                FileExplorer.Items.Add(subdir.Split("\").Last.ToString + "\")
            Next
            For Each file1 In Directory.EnumerateFiles(pathbox.Text())
                Dim flag1 = False
                For Each currentitem In watchdict.Keys()
                    If currentitem = file1 Then
                        flag1 = True
                    End If
                Next
                If flag1 = False Then
                    FileExplorer.Items.Add(file1.Split("\").Last.ToString)
                End If
            Next
        ElseIf pathbox.Text = "" Then
            load_explorer()
        End If
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        If Not FileExplorer.SelectedItem = "..." And Not FileExplorer.SelectedItem = "" Then
            Try
                If FileExplorer.SelectedItem.ToString.ToCharArray.Last() = "\" Then
                    Dim choice = MsgBox("Would you like to include subdirectories as well?", MsgBoxStyle.YesNoCancel, FileExplorer.SelectedItem.ToString)

                    If choice = MsgBoxResult.Yes Then
                        watchdict.Add(pathbox.Text.ToString + FileExplorer.SelectedItem.ToString, "SD")
                        Clean_watchlist()
                        Refresh_Watchlistbox()
                    ElseIf choice = MsgBoxResult.No Then
                        watchdict.Add(pathbox.Text.ToString + FileExplorer.SelectedItem.ToString, "D")
                        Clean_watchlist()
                        Refresh_Watchlistbox()
                    ElseIf choice = MsgBoxResult.Cancel Then

                    End If
                Else
                    watchdict.Add(pathbox.Text.ToString + FileExplorer.SelectedItem.ToString, "F")
                    Clean_watchlist()
                    Refresh_Watchlistbox()
                End If
            Catch
            End Try
        End If

    End Sub




    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click

    End Sub

    Private Sub load_watchpath()
        watchlist.Items.Clear()
        Dim allDrives() As DriveInfo = DriveInfo.GetDrives()
        Dim d As DriveInfo
        For Each d In allDrives
            If d.IsReady = True Then
                watchlist.Items.Add(d.Name.ToString())
            End If
        Next
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        watchdict.Remove(watchlist.SelectedItem.ToString)
        Refresh_Watchlistbox()
        pathbox_TextChanged()
    End Sub


    Private Sub watchpath_TextChanged(sender As Object, e As EventArgs) Handles watchpath.TextChanged
        Refresh_Watchlistbox()
    End Sub
End Class


