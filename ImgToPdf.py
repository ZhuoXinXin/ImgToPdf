# coding=utf-8
import wx
import os
from PIL import Image


class ImgToPdf(wx.Frame):

    
    def __init__(self):
        wx.Frame.__init__(self,None,title='图片生成PDF器',size=(500,400))


        self.url_text = wx.TextCtrl(self, pos=(5, 5), size=(350, 24), value="请选择目录")
        
        self.select_button = wx.Button(self, label="选择目录", pos=(370, 5), size=(80, 24))
        self.select_button.Bind(wx.EVT_BUTTON, self.OnButton)
        
        self.open_button = wx.Button(self, label="生成", pos=(5, 30), size=(50, 24))
        self.open_button.Bind(wx.EVT_BUTTON, self.conpdf)

        self.content_text = wx.TextCtrl(self, pos=(5, 55), size=(475, 200), style=wx.TE_MULTILINE)

        
    # 生成PDF
    def conpdf(self, event):
        self.content_text.AppendText("开始生成pdf\n")
        # 获取图片文件夹所在路径
        path = self.url_text.GetValue()
        pdf_name = os.path.basename(path)
        picList = []
        picType = ['.jpg', '.jpeg', '.bmp', '.png', '.gif']
        
        # 遍历图片文件夹内的图片，生成图片列表
        file_list = os.listdir(path)
        pic_name = []
        im_list = []
        for x in file_list:
            if "jpg" in x or 'png' in x or 'jpeg' in x:

                pic_name.append(x)

        pic_name.sort()
        new_pic = []
        
        for x in pic_name:
            if "jpg" in x:
                new_pic.append(x)

        for x in pic_name:
            if "png" in x:
                new_pic.append(x)
                
        for x in pic_name:
            if "jpeg" in x:
                new_pic.append(x)            
        
        # 打开第一张图片，并删除图片列表中第一张图片
        im1 = Image.open(os.path.join(path, new_pic[0]))
        if im1.mode == "RGBA":
            im1 = im1.convert('RGB')
        new_pic.pop(0)
        
        # 将图片打开分别添加至im_list
        for i in new_pic:
            img = Image.open(os.path.join(path, i))
            if img.mode == "RGBA":
                img = img.convert('RGB')
                im_list.append(img)
            else:
                im_list.append(img)

        # 将首张图片添加im_list，并保存为pdf至程序所在目录
        im1.save(pdf_name+'.pdf', "PDF", resolution=100.0, save_all=True, append_images=im_list)
        self.content_text.AppendText("生成pdf完成\n")
        self.content_text.AppendText("================================\n")
        
    # 选择文件夹
    def OnButton(self, event):

            dlg = wx.DirDialog(self,u"选择文件夹",style=wx.DD_DEFAULT_STYLE)
            if dlg.ShowModal() == wx.ID_OK:
                print(dlg.GetPath()) #文件夹路径
                self.url_text.SetValue(dlg.GetPath())
            dlg.Destroy()



if __name__=='__main__':
    app = wx.App()
    ImgToPdfFrame = ImgToPdf()
    ImgToPdfFrame.Show()
    app.MainLoop()

