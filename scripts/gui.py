import wx
from PIL import Image
import time
from generateclass import Generate

class ContextDirDialog(wx.DirDialog):

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Destroy()

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Pinilian Pattern Generator')
        panel = wx.Panel(self)        

        my_sizer = wx.BoxSizer(wx.VERTICAL)
        sizer2 = wx.BoxSizer(wx.HORIZONTAL)    

        self.SizeText = wx.StaticText(panel, label="Choose size of canvas below:", style=wx.ALIGN_CENTRE_HORIZONTAL)
        my_sizer.Add(self.SizeText, 0, wx.ALL | wx.CENTER, 5)

        sizeChoices = [ "Small", "Medium", "Large" ]
        self.mySize = wx.Choice(panel, wx.ID_ANY, choices=sizeChoices)
        self.mySize.SetSelection(0)
        my_sizer.Add(self.mySize, 0, wx.CENTER, 5)

        self.ColorAText = wx.StaticText(panel, label="Pick your primary color below:", style=wx.ALIGN_CENTRE_HORIZONTAL)
        my_sizer.Add(self.ColorAText, 0, wx.ALL | wx.CENTER, 5)

        self.ColorA = wx.ColourPickerCtrl(panel, wx.ID_ANY)
        my_sizer.Add(self.ColorA, 0, wx.CENTER, 5)

        self.ColorBText = wx.StaticText(panel, label="Pick your background color below:", style=wx.ALIGN_CENTRE_HORIZONTAL)
        my_sizer.Add(self.ColorBText, 0, wx.ALL | wx.CENTER, 5)

        self.ColorB = wx.ColourPickerCtrl(panel, wx.ID_ANY, colour=(255,255,255))
        my_sizer.Add(self.ColorB, 0, wx.CENTER, 5)

        self.PNGbutton = wx.Button(panel, label="PNG", size=(100,40))
        self.PNGbutton.Bind(wx.EVT_BUTTON, self.on_pressPNG)
        sizer2.Add(self.PNGbutton, 0, wx.ALL | wx.CENTER, 5)     

        self.GIFbutton = wx.Button(panel, label="GIF", size=(100,40))
        self.GIFbutton.Bind(wx.EVT_BUTTON, self.on_pressGIF)
        sizer2.Add(self.GIFbutton, 0, wx.ALL | wx.CENTER, 5)

        self.GenerateText = wx.StaticText(panel, label="Generate pattern as:", style=wx.ALIGN_CENTRE_HORIZONTAL)
        my_sizer.Add(self.GenerateText, 0, wx.ALL | wx.CENTER, 5)

        my_sizer.Add(sizer2, 0, wx.CENTER,5)    

        panel.SetSizer(my_sizer)

        self.Show()
    
    def on_pressPNG(self, event):
        #create PNG on a directory, put update on log
        szstr = self.mySize.GetCurrentSelection()
        if szstr == 0:
            sz = 17
        elif szstr == 1:
            sz = 23
        elif szstr == 2:
            sz = 27
        clrA = tuple(self.ColorA.GetColour())
        clrB = tuple(self.ColorB.GetColour())

        gen = Generate(sz,clrA,clrB)
        ctime = time.localtime()

        with ContextDirDialog(self, message="Save to:",
                              style=wx.DD_DIR_MUST_EXIST) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                drect = dlg.GetPath()
                print("drect")
                board = gen.generatePNG()
                print("board oakay")
                board.save(drect + "\\" + "PNG" + str(ctime.tm_sec) + str(ctime.tm_min) + str(ctime.tm_hour) + str(ctime.tm_mday) + str(ctime.tm_mon) + str(ctime.tm_year) +".png", format='PNG')
                print("boarsave")
                wx.MessageBox('PNG Generated.', 'Prompt', wx.OK | wx.ICON_INFORMATION)
                print("end")
            else:
                wx.LogError("Didn't specify directory.")


    def on_pressGIF(self, event):
        #create GIF on a directory, put update on log
        szstr = self.mySize.GetCurrentSelection()
        if szstr == 0:
            sz = 17
        elif szstr == 1:
            sz = 23
        elif szstr == 2:
            sz = 27
        clrA = tuple(self.ColorA.GetColour())
        clrB = tuple(self.ColorB.GetColour())

        gen = Generate(sz,clrA,clrB)
        ctime = time.localtime()

        with ContextDirDialog(self, message="Save to:",
                              style=wx.DD_DIR_MUST_EXIST) as dlg:          
            if dlg.ShowModal() == wx.ID_OK:
                drect = dlg.GetPath()
                frames = gen.generateGIF()
                frames[0].save(drect + "\\" + "GIF" + str(ctime.tm_sec) + str(ctime.tm_min) + str(ctime.tm_hour) + str(ctime.tm_mday) + 
                    str(ctime.tm_mon) + str(ctime.tm_year) +".gif", format='GIF', save_all=True, append_images=frames[1:], duration=90, loop=0)
                wx.MessageBox('GIF Generated.', 'Prompt', wx.OK | wx.ICON_INFORMATION)
            else:
                wx.LogError("Didn't specify directory.")
        
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()