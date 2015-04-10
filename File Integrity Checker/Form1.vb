Imports System
Imports System.IO

Public Class Form1


    Dim userpath = "users.txt"
    Dim prevdir As String
    Dim watchlistpath = "watchlist.txt"
    Dim watchlist As New List(Of String)
    Dim watchflag = False
    Dim FileList as New List(of String)
    
    Private Sub Check_files()
        If not My.Computer.FileSystem.FileExists(watchlistpath) Then
            Dim fs As FileStream = File.Create(watchlistpath)
            fs.Close()
            watchflag = True
        End If
        If not My.Computer.FileSystem.FileExists(userpath) Then
            Dim fs As FileStream = File.Create(userpath)
            fs.Close()
        End If
    End Sub
    
    Private Sub Clean_watchlist()
        For Each item in watchlist
            For Each item2 in watchlist
                If item = item2 Then
                    watchlist.Items.Remove(watchlist.Items.Indexof(item))
                End If
            Next
        Next
    End Sub 
    
    Private Sub Refresh_Watchlistbox()
        For Each item in watchlist
            watchlistbox.Items.Add(item)
        Next
    End Sub
    
    Private Sub Load_Watchlist()
        For each file in File.Readlines
            for each curfile in watchlist.Items()
                If not file = curfile Then
                    watchlist.Items.add(file)
                End If
            Next
        Next
    End Sub
    
    Private Sub Load_All_Files()
        Dim allDrives() As DriveInfo = DriveInfo.GetDrives()
        Dim d As DriveInfo
        For Each d In allDrives
            If d.IsReady = True Then
                For each file1 in Directory.EnumerateFiles(drive)
                    FileList.Items.Add()
                Next

            End If
        Next

    End Sub
    
    Private Sub SearchFiles()
        For Each file1 in 
    End Sub
    
    Private Sub Refresh_click(sender As Object, e As EventArgs) Handles Refresh.Click()
        If Directory.Exists(pathbox.Text.ToString) Then
            FileExplorer.Items.Clear()
            If Not pathbox.Text.ToString.Length = 3 Then
                FileExplorer.Items.add("...")
                For Each subdir in Directory.EnumerateDirectories(pathbox.Text.ToString) Then
                    FileExplorer.Items.Add(subdir)
                Next
                For Each file1 in Directory.EnumerateFiles(pathbox.Text.ToString)
                    FileExplorer.Items.Add(file1)
                Next
            End If
        Else If pathbox.Text.ToString.Contains("\") = False Then
            SearchFiles()
        Else
            MsgBox("Directory does not exsist. Check the path and try again.")
        End If    

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Me.Size = New Size(400, 200)
        draw_login_buttons()
        Check_files()
        If watchflag = False Then
            Load_Watchlist()
        Else
            watchlist.Items.Add("")
        End If
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
            Dim newdir = Directory.GetParent(pathbox.Text)
            If pathbox.Text.Length = 3 Then
                pathbox.Text = ""
            Else
                pathbox.Text = newdir.ToString()
            End If
        Else
            pathbox.Text = FileExplorer.SelectedItem.ToString()
        End If
    End Sub


    Private Sub pathbox_TextChanged(sender As Object, e As EventArgs) Handles pathbox.TextChanged
        If Directory.Exists(pathbox.Text) = True Then
            FileExplorer.Items.Clear()
            If Not pathbox.Text.Split("\").Length = 1 Then
                FileExplorer.Items.Add("...")
            End If
            For Each subdir In Directory.EnumerateDirectories(pathbox.Text())
                FileExplorer.Items.Add(subdir)
            Next
            For Each file1 In Directory.EnumerateFiles(pathbox.Text())
            Dim flag1 = False
                For Each currentitem in watchlist
                    If currentitem = file1 Then
                        flag1 = True
                    End If
                Next
                If flag1 = False Then
                    FileExplorer.Items.Add(file1)
                End If
            Next
        ElseIf pathbox.Text = "" Then
            load_explorer()
        End If
    End Sub
End Class
