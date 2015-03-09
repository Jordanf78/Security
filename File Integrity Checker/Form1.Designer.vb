<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.LocalSignin = New System.Windows.Forms.Button()
        Me.GoogleLoginButton = New System.Windows.Forms.Button()
        Me.CreateNewButton = New System.Windows.Forms.Button()
        Me.usernamebox = New System.Windows.Forms.TextBox()
        Me.UsernameLabel = New System.Windows.Forms.Label()
        Me.Passwordbox = New System.Windows.Forms.TextBox()
        Me.passwordlabel = New System.Windows.Forms.Label()
        Me.LoginButton = New System.Windows.Forms.Button()
        Me.Create = New System.Windows.Forms.Button()
        Me.BackButton = New System.Windows.Forms.Button()
        Me.ChangeLogBox = New System.Windows.Forms.ListBox()
        Me.FileExplorer = New System.Windows.Forms.ListBox()
        Me.SuspendLayout()
        '
        'LocalSignin
        '
        Me.LocalSignin.Font = New System.Drawing.Font("Microsoft Sans Serif", 11.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LocalSignin.Location = New System.Drawing.Point(75, 12)
        Me.LocalSignin.Name = "LocalSignin"
        Me.LocalSignin.Size = New System.Drawing.Size(250, 41)
        Me.LocalSignin.TabIndex = 0
        Me.LocalSignin.Text = "Sign In to Local Account"
        Me.LocalSignin.UseVisualStyleBackColor = True
        '
        'GoogleLoginButton
        '
        Me.GoogleLoginButton.Font = New System.Drawing.Font("Microsoft Sans Serif", 11.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.GoogleLoginButton.Location = New System.Drawing.Point(75, 59)
        Me.GoogleLoginButton.Name = "GoogleLoginButton"
        Me.GoogleLoginButton.Size = New System.Drawing.Size(250, 41)
        Me.GoogleLoginButton.TabIndex = 1
        Me.GoogleLoginButton.Text = "Sign In to Google Account"
        Me.GoogleLoginButton.UseVisualStyleBackColor = True
        '
        'CreateNewButton
        '
        Me.CreateNewButton.Font = New System.Drawing.Font("Microsoft Sans Serif", 9.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.CreateNewButton.Location = New System.Drawing.Point(125, 124)
        Me.CreateNewButton.Name = "CreateNewButton"
        Me.CreateNewButton.Size = New System.Drawing.Size(150, 26)
        Me.CreateNewButton.TabIndex = 2
        Me.CreateNewButton.Text = "Create Local Account"
        Me.CreateNewButton.UseVisualStyleBackColor = True
        '
        'usernamebox
        '
        Me.usernamebox.Location = New System.Drawing.Point(123, 24)
        Me.usernamebox.Name = "usernamebox"
        Me.usernamebox.Size = New System.Drawing.Size(249, 20)
        Me.usernamebox.TabIndex = 3
        Me.usernamebox.Visible = False
        '
        'UsernameLabel
        '
        Me.UsernameLabel.AutoSize = True
        Me.UsernameLabel.Font = New System.Drawing.Font("Microsoft Sans Serif", 12.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.UsernameLabel.Location = New System.Drawing.Point(12, 24)
        Me.UsernameLabel.Name = "UsernameLabel"
        Me.UsernameLabel.Size = New System.Drawing.Size(83, 20)
        Me.UsernameLabel.TabIndex = 4
        Me.UsernameLabel.Text = "Username"
        Me.UsernameLabel.Visible = False
        '
        'Passwordbox
        '
        Me.Passwordbox.Location = New System.Drawing.Point(123, 59)
        Me.Passwordbox.Name = "Passwordbox"
        Me.Passwordbox.Size = New System.Drawing.Size(249, 20)
        Me.Passwordbox.TabIndex = 5
        Me.Passwordbox.Visible = False
        '
        'passwordlabel
        '
        Me.passwordlabel.AutoSize = True
        Me.passwordlabel.Font = New System.Drawing.Font("Microsoft Sans Serif", 12.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.passwordlabel.Location = New System.Drawing.Point(17, 59)
        Me.passwordlabel.Name = "passwordlabel"
        Me.passwordlabel.Size = New System.Drawing.Size(78, 20)
        Me.passwordlabel.TabIndex = 6
        Me.passwordlabel.Text = "Password"
        Me.passwordlabel.Visible = False
        '
        'LoginButton
        '
        Me.LoginButton.Font = New System.Drawing.Font("Microsoft Sans Serif", 11.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LoginButton.Location = New System.Drawing.Point(75, 109)
        Me.LoginButton.Name = "LoginButton"
        Me.LoginButton.Size = New System.Drawing.Size(250, 41)
        Me.LoginButton.TabIndex = 7
        Me.LoginButton.Text = "Login"
        Me.LoginButton.UseVisualStyleBackColor = True
        Me.LoginButton.Visible = False
        '
        'Create
        '
        Me.Create.Font = New System.Drawing.Font("Microsoft Sans Serif", 11.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Create.Location = New System.Drawing.Point(75, 109)
        Me.Create.Name = "Create"
        Me.Create.Size = New System.Drawing.Size(250, 41)
        Me.Create.TabIndex = 8
        Me.Create.Text = "Submit"
        Me.Create.UseVisualStyleBackColor = True
        Me.Create.Visible = False
        '
        'BackButton
        '
        Me.BackButton.Font = New System.Drawing.Font("Microsoft Sans Serif", 11.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.BackButton.Location = New System.Drawing.Point(12, 109)
        Me.BackButton.Name = "BackButton"
        Me.BackButton.Size = New System.Drawing.Size(57, 41)
        Me.BackButton.TabIndex = 9
        Me.BackButton.Text = "Back"
        Me.BackButton.UseVisualStyleBackColor = True
        Me.BackButton.Visible = False
        '
        'ChangeLogBox
        '
        Me.ChangeLogBox.FormattingEnabled = True
        Me.ChangeLogBox.Location = New System.Drawing.Point(422, 24)
        Me.ChangeLogBox.Name = "ChangeLogBox"
        Me.ChangeLogBox.Size = New System.Drawing.Size(325, 342)
        Me.ChangeLogBox.TabIndex = 10
        Me.ChangeLogBox.Visible = False
        '
        'FileExplorer
        '
        Me.FileExplorer.FormattingEnabled = True
        Me.FileExplorer.Location = New System.Drawing.Point(16, 24)
        Me.FileExplorer.Name = "FileExplorer"
        Me.FileExplorer.Size = New System.Drawing.Size(325, 342)
        Me.FileExplorer.TabIndex = 11
        Me.FileExplorer.Visible = False
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(784, 562)
        Me.Controls.Add(Me.FileExplorer)
        Me.Controls.Add(Me.ChangeLogBox)
        Me.Controls.Add(Me.BackButton)
        Me.Controls.Add(Me.Create)
        Me.Controls.Add(Me.LoginButton)
        Me.Controls.Add(Me.passwordlabel)
        Me.Controls.Add(Me.Passwordbox)
        Me.Controls.Add(Me.UsernameLabel)
        Me.Controls.Add(Me.usernamebox)
        Me.Controls.Add(Me.CreateNewButton)
        Me.Controls.Add(Me.GoogleLoginButton)
        Me.Controls.Add(Me.LocalSignin)
        Me.Name = "Form1"
        Me.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
        Me.Text = "File Integrity Checker"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents LocalSignin As System.Windows.Forms.Button
    Friend WithEvents GoogleLoginButton As System.Windows.Forms.Button
    Friend WithEvents CreateNewButton As System.Windows.Forms.Button
    Friend WithEvents usernamebox As System.Windows.Forms.TextBox
    Friend WithEvents UsernameLabel As System.Windows.Forms.Label
    Friend WithEvents Passwordbox As System.Windows.Forms.TextBox
    Friend WithEvents passwordlabel As System.Windows.Forms.Label
    Friend WithEvents LoginButton As System.Windows.Forms.Button
    Friend WithEvents Create As System.Windows.Forms.Button
    Friend WithEvents BackButton As System.Windows.Forms.Button
    Friend WithEvents ChangeLogBox As System.Windows.Forms.ListBox
    Friend WithEvents FileExplorer As System.Windows.Forms.ListBox

End Class
