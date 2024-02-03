"""MenstruGuide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from DiscussionForum import views
from PCOS_Prediction import views as pview
from Awareness import views as vi
from Trackers import views as vt
from home import views as vh
from accounts import views as vac
from product import views as vp

urlpatterns = [
    
    path('',vh.homePg),
    path('admin/',admin.site.urls),
    path('registerform',vh.registerform),
    path('loginform',vh.loginform),
    path('discussionForum', views.DiscussionForm),
    path('discussionForum/data/my_func',views.DiscussionData),
    path('pcosHome', pview.home),
    path('pcosPredict', pview.predict),
    path('result',pview.result),
    path('nextPeriod', vt.nextPeriod),
    path('ovulation', vt.ovulation),
    path('pregnancyTracker', vt.pregnancyTracker),
    # path('login',vh.login),
    path('login', vac.login_page, name="login"),
    path('MenstrualAwareness',vi.MenstrualAwareness),
    path('absenceOfPeriods',vi.absenceOfPeriods),
    path('acneBreakout',vi.acneBreakout),
    path('adaptgoodskin',vi.adaptgoodskin),
    path('anemia',vi.anemia),
    path('bodyBreakouts',vi.bodyBreakouts),
    path('contact',vi.contact),
    path('doDont',vi.doDont),
    path('dryness',vi.dryness),
    path('hairchange',vi.hairchange),
    path('healthyHair',vi.healthyHair),
    path('homeRemedies',vi.homeRemedies),
    path('hygiene',vi.hygiene),
    path('irregularPeriods',vi.irregularPeriods),
    path('lightPeriods',vi.lightPeriods),
    path('menopause',vi.menopause),
    path('menstrualPainHR',vi.menstrualPainHR),
    path('oilyhair',vi.oilyhair),
    path('overcomeDarkSpot',vi.overcomeDarkSpot),
    path('overcomeDryness',vi.overcomeDryness),
    path('premenstrual',vi.premenstrual),
    path('protectSkin',vi.protectSkin),
    path('rashes',vi.rashes),
    path('sheddingOfHairs',vi.sheddingOfHairs),
    path('skinChange',vi.skinChange),
    path('skinProblems',vi.skinProblems),
    path('vaginalInfectionsHR',vi.vaginalInfectionsHR),
    path('vaginalItching',vi.vaginalItching),
    path('whyacne',vi.whyacne),
    path('whyacneoccurs',vi.whyacneoccurs),
    path('whylate',vi.whylate),
    path('yoga',vi.yoga),
    path('quiz',vi.quiz),
    path('accounts/',include('accounts.urls')),
    path('productHome',vp.productHome),
    path('getProducts',vp.get_product),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()