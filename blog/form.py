#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from models import Comment,Article
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
