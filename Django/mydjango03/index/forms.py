# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/2/25 9:33
# @File_name:forms.py
# @IDE:PyCharm

from django import forms
from .models import *


# 表示一个评论内容的表单控件
class RemarkForm(forms.Form):
    """
    控件1 - 评论标题subject - 文本框
    控件2 - Email - Email框
    控件3 - 评论内容message - Textarea
    控件4 - 评论级别 level - Select，并初始化数据
    控件5 - 是否保存 isSaved - Checkbox
    """
    subject = forms.CharField(label='标题')
    email = forms.EmailField(label='邮箱')
    message = forms.CharField(label="评论内容", widget=forms.Textarea)
    level = forms.ChoiceField(label='评论级别', choices=(
        ('1', '好评'),
        ('2', '一般'),
        ('3', '差评'),
    ))
    isSaved = forms.BooleanField(label='是否保存')


# 创建注册表单类
class RegisterForm(forms.Form):
    uname = forms.CharField(label="用户名")
    upwd = forms.CharField(label="密码", widget=forms.PasswordInput)
    uage = forms.IntegerField(label="年龄")
    uemail = forms.EmailField(label="邮箱")


class AuthorForm(forms.ModelForm):
    class Meta:
        # 1. 指定关联的Model类
        model = Author
        # 2. 指定从Model类中取得那些属性生成控件
        fields = '__all__'
        # 3. 指定model类中的属性对应的lable标签
        labels = {
            'name': "姓名",
            'age': "年龄",
            'email': "邮箱",
            "isActive": "激活",
        }


class WidgetForm(forms.Form):
    # uname: 用户名， placeholder：请输入用户名，class：form-input
    uname = forms.CharField(label="用户名", widget=forms.TextInput(attrs={
        "placeholder": "请输入用户名",
        "class": "form-input"
    }))
    # upwd: 密码， placeholder：请输入密码，class：form-input
    upwd = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={
        "placeholder": "请输入密码",
        "class": "form-input"
    }))


class WidgetModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','email']
        labels = {
            'name':"姓名",
            'email':"邮箱",
        }
        widgets = {
            'name':forms.TextInput(
                attrs={
                    'placeholder':'请输入姓名',
                    'class':"form-input",
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'placeholder':"请输入邮箱",
                    'class':'form-input',
                }
            ),
        }
