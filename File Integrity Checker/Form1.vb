Imports System
Imports System.IO

Public Class Form1


    Dim userpath = "users.txt"



    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Me.Size = New Size(400, 200)
        draw_login_buttons()
        checkuserfile()
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
        ChangeLogBox.Visible = False
        FileExplorer.Visible = False

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

    Private Sub checkuserfile()
        If Not System.IO.File.Exists(userpath) Then
            Dim ope = System.IO.File.Create(userpath)
            ope.Close()
        End If
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
        ChangeLogBox.Visible = True
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
                Dim string1 As String = d.Name.ToString + vbTab + d.VolumeLabel.ToString
                FileExplorer.Items.Add(string1)
            End If
        Next
    End Sub

    Private Sub FileExplorer_SelectedIndexChanged(sender As Object, e As EventArgs) Handles FileExplorer.SelectedIndexChanged

    End Sub
End Class
