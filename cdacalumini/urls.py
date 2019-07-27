from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from .views import *
from .forms import ContactForm1,ContactForm2,ContactForm3,ContactForm4

urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'^login/$', login_c, name='login_c'),
    url(r'^infov/$', infov, name='infov'),
    url(r'^register/$', register_c, name='register_c'),
    url(r'^registeru/$', register_u, name='ru'),
    url(r'^registere/$', register_e, name='re'),
    url(r'^registerp/$', register_p, name='rp'),

    url(r'^contact/$', contact, name='contact'),
    url(r'^about/$', about, name='about'),
    url(r'^roleinfo/$', ContactWizard.as_view([ContactForm1,ContactForm2,ContactForm3,ContactForm4])),
    url(r'^logout/$', logout_c, name='logout_c'),
    url(r'^done/$', pdone, name='done'),
    url(r'^demo/$', postjob, name='demo'),
    url(r'^batch/$', batch, name='batch'),
    url(r'^single/(?P<id>\d+)/$',single,name='single'),
    url('^',include('django.contrib.auth.urls')),
    url(r'^year/$', yearbook, name='yearbook'),
    url(r'^b2019/$',b2019, name='b2019'),
    url(r'^b2018/$',b2018, name='b2018'),
    url(r'^b2017/$',b2017, name='b2017'),
    url(r'^b2016/$',b2016, name='b2016'),
    url(r'^b2015/$',b2015, name='b2015'),
    url(r'^b2014/$',b2014, name='b2014'),
    url(r'^b2013/$',b2013, name='b2013'),
    url(r'^b2012/$',b2012, name='b2012'),
    url(r'^b2011/$',b2011, name='b2011'),
    url(r'^b2010/$',b2010, name='b2010'),
    url(r'^b2009/$',b2009, name='b2009'),
    url(r'^b2008/$',b2008, name='b2008'),
    url(r'^job/$',job, name='job'),
    url(r'^my_profile/$', my_profile, name='my_profile'),
    url(r'^director/$', director, name='director'),
    url(r'^jobdetail/(?P<id>\d+)/$',jobdetail, name='jobdetail'),
    url(r'^applied_by_me/$', applied_by_me, name='applied_by_me'),
    url(r'^applyjob/(?P<id>\d+)/$', applyjob, name='applyjob'),
    url(r'^postedjob/$', postedjob, name='postedjob'),
    url(r'^singlepostedjob/(?P<id>\d+)/$', singlepostedjob, name='singlepostedjob'),
    url(r'^get/(?P<id>\d+)/$',getfile, name='getfile'),
    url(r'^users/$', users_list, name='list'),
    url(r'^prof/(?P<id>[\w-]+)/$', profile_view),
    url(r'^friend-request/send/(?P<id>[\w-]+)/$', send_friend_request),
    url(r'^friend-request/cancel/(?P<id>[\w-]+)/$', cancel_friend_request),
    url(r'^friend-request/send0/(?P<id>[\w-]+)/(?P<name>\w+)/$', send_friend_request0),
    url(r'^friend-request/cancel0/(?P<id>[\w-]+)/(?P<name>\w+)/$', cancel_friend_request0),
    url(r'^friend-request/send1/(?P<id>[\w-]+)/(?P<id2>[\w-]+)/$', send_friend_request1),
    url(r'^friend-request/cancel1/(?P<id>[\w-]+)/(?P<id2>[\w-]+)/$', cancel_friend_request1),
    url(r'^friend-request/accept/(?P<id>[\w-]+)/$', accept_friend_request),
    url(r'^friend-request/delete/(?P<id>[\w-]+)/$', delete_friend_request),
    url(r'^uprof/(?P<user>\w+)/$',uprof,name='uprof'),
    url(r'^allfriends/$', allfriends, name='allfriends'),
    url(r'^form/(?P<u>\w+|)/$',messageview,name='messageview'),
    url(r'^form/(?P<u>\w+|)/$', messageviewn, name='messageviewn'),

    url(r'^delete_message/(?P<id>\d+)/$',delete_message, name='delete_message'),
    url(r'^edit/(?P<id>\d+)/$', piceditv, name='piceditv'),
    url(r'^editcontact/(?P<id>\d+)/$', editcontact, name='editcontact'),
    url(r'^editedu/(?P<id>\d+)/$', edueditv, name='edueditv'),
    url(r'^editexpert/(?P<id>\d+)/$', experteditv, name='experteditv'),
    url(r'^uprof1/(?P<id>\d+)/$', uprof1, name='uprof1'),
    url(r'^login1/$',login_v, name='login_v'),
    url(r'^prev1/$', prev1, name='prev1'),
    url(r'^prev2/$', prev2, name='prev2'),
    url(r'^prev3/$', prev3, name='prev3'),
    url(r'^validp/$', validp, name='validp'),
    url(r'^validj/$', validj, name='validj'),
    url(r'^a/$', get_document, name='get_document'),
    url(r'^search/$', search, name='search'),
    url(r'^friend-request_s/send/(?P<id>[\w-]+)/(?P<querry>\w+)/$', send_friend_request_s),
    url(r'^friend-request_s/cancel/(?P<id>[\w-]+)/(?P<querry>\w+)/$', cancel_friend_request_s),
    url(r'^search/(?P<querry>\w+)/$', search, name='sea'),
    url(r'^friend-request_p/send/(?P<id>[\w-]+)/(?P<querry>\w+)/$', send_friend_request_p),
    url(r'^friend-request_p/cancel/(?P<id>[\w-]+)/(?P<querry>\w+)/$', cancel_friend_request_p),
    url(r'^searchp/(?P<querry>\w+)/$', searchp, name='seap'),
    url(r'^searchp/$', searchp, name='searchp'),
    url(r'^searchj/$', searchj, name='searchj'),
    url(r'^network/$', network, name='network'),
    url(r'^message/$', message, name='message'),
    url(r'^yeart/$', yeart, name='yeart'),
    url(r'^b2019t/$', b2019t, name='b2019t'),
    url(r'^b2018t/$', b2018t, name='b2018t'),
    url(r'^b2017t/$', b2017t, name='b2017t'),
    url(r'^b2016t/$', b2016t, name='b2016t'),
    url(r'^b2015t/$', b2015t, name='b2015t'),
    url(r'^b2014t/$', b2014t, name='b2014t'),
    url(r'^b2013t/$', b2013t, name='b2013t'),
    url(r'^b2012t/$', b2012t, name='b2012t'),
    url(r'^b2011t/$', b2011t, name='b2011t'),
    url(r'^b2010t/$', b2010t, name='b2010t'),
    url(r'^b2009t/$', b2009t, name='b2009t'),
    url(r'^b2008t/$', b2008t, name='b2008t'),
    url(r'^sdata/(?P<id>\d+)/$', sdata, name='sdata'),
    url(r'^searcht/$', search_text, name='search_text'),
    url(r'^rmaker/$', resumemaker, name='rmake'),
    url(r'^rjob/$', rjob, name='rjob'),
    url(r'^rpro/$', rpro, name='rpro'),
    url(r'^rint/$', rint, name='rint'),
    url(r'^rtra/$', rtra, name='rtra'),
    url(r'^rskill/$', rskill, name='rpro'),
    url(r'^ajax/validate_username/$',validate_username, name='validate_username'),
    url(r'^ajax/validate_email/$', validate_email, name='validate_email'),
    url(r'^ajax/validate_skill/$', validate_skill, name='skillvalid'),
    url(r'^ajax/validate_date/$', validate_date, name='datevalid'),
    url(r'^ajax/validate_datei/$', validate_datei, name='datevalidi'),
    url(r'^ajax/validate_datet/$', validate_datet, name='datevalidt'),
    url(r'^ajax/validate_datej/$', validate_datej, name='datevalidj'),
    url(r'^ajax/validate_datee/$', validate_datee, name='datevalid'),
    url(r'^ajax/validate_dateie/$', validate_dateie, name='datevalidi'),
    url(r'^ajax/validate_datete/$', validate_datete, name='datevalidt'),
    url(r'^ajax/validate_dateje/$', validate_dateje, name='datevalidj'),
    url(r'^skilledit/(?P<id>\d+)/$', skilleditv, name='skilleditv'),
    url(r'^trainedit/(?P<id>\d+)/$', traineditv, name='traineditv'),
    url(r'^proedit/(?P<id>\d+)/$', proeditv, name='proeditv'),
    url(r'^internedit/(?P<id>\d+)/$', interneditv, name='interneditv'),
    url(r'^jobedit/(?P<id>\d+)/$', jobeditv, name='jobeditv'),
    url(r'^tresume/(?P<id>\d+)/$',tresume, name='tresume'),
    url(r'^deljob/(?P<id>[\w-]+)/$', deletejob),
    url(r'^delskill/(?P<id>[\w-]+)/$', deleteskill),
    url(r'^deltrain/(?P<id>[\w-]+)/$', deletetrain),
    url(r'^delint/(?P<id>[\w-]+)/$', deleteint),
    url(r'^delpro/(?P<id>[\w-]+)/$', deletepro),
    url(r'^postjobt/$', postjobt, name='postjobt'),
    url(r'^ajax/validatecn/$', validatecn, name='validcn'),
    url(r'^ajax/validateuser/$', validateuser, name='validuser'),
    url(r'^ajax/validatejt/$', validatejt, name='validjt'),
    url(r'^ajax/validateloc/$', validateloc, name='validloc'),
    url(r'^ajax/validateac/$', validateac, name='validac'),
    url(r'^ajax/validatear/$', validatear, name='validar'),
    url(r'^delete_messagen/(?P<id>\d+)/$', delete_messagen, name='delete_messagen'),

]