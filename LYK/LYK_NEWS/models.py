
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
a=dir(models)

class NewsItem(models.Model):
	TURKEY="TR"
	SWEDEN="SWE"
	ENGLAND="ENG"
	Choices_Set=[(TURKEY,"TURKEY"),(ENGLAND,"ENGLAND"),(SWEDEN,"SWEDEN"),(None,"Bunu göster")]
	tittle=models.CharField(max_length=3,error_messages={"invalid":"asagdafs"})
	date_creation=models.DateTimeField(auto_now_add=False,error_messages={"invalid":"ahaha"})	
	news_locale=models.CharField(max_length=3,choices=Choices_Set)
	content=models.TextField(default="")
# Create your models here.
