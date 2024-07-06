from urllib import request

import django
import self
from django.contrib.messages import get_messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic import ListView

from . import models
from .models import UpdateProfile, EmailField, Answer, FeedbackBackgroundImage, TradeItem, TradeOffer, Shuffler, \
    PrizePool, CurrencyMarket, CurrencyOrder, SellerApplication, Meme, CurrencyFullOrder, Currency, Wager, GameHub, \
    InventoryObject, Inventory, Trade, FriendRequest, Friend, RespondingTradeOffer, TradeShippingLabel, \
    Game, UploadACard, Withdraw, ExchangePrize, CommerceExchange, SecretRoom, Transaction, Outcome
from .models import Idea
from .models import Vote
from .models import StaffApplication
from .models import Contact
from .models import BusinessMailingContact
from .models import PartnerApplication
from .models import PunishmentAppeal
from .models import BanAppeal
from .models import ReportIssue
from .models import NewsFeed
from .models import StaffProfile
from .models import Event
from .models import City, Vote, UpdateProfile, Idea, PartnerApplication
from .models import ItemFilter
from .models import Support
from .models import CheckoutAddress
from .models import Item
from .models import FaviconBase
from .models import BackgroundImage
from .models import EBackgroundImage
from .models import ShowcaseBackgroundImage
from .models import ChatBackgroundImage
from .models import SupportChatBackgroundImage
from .models import BilletBackgroundImage
from .models import PatreonBackgroundImage
from .models import BusinessMessageBackgroundImage
from .models import Patreon
from .models import StoreViewType
from .models import BlogBackgroundImage
from .models import PostBackgroundImage
from .models import PosteBackgroundImage
from .models import VoteBackgroundImage
from .models import RuleBackgroundImage
from .models import AboutBackgroundImage
from .models import FaqBackgroundImage
from .models import StaffBackgroundImage
from .models import InformationBackgroundImage
from .models import TagBackgroundImage
from .models import UserBackgroundImage
from .models import StaffRanksBackgroundImage
from .models import StaffApplyBackgroundImage
from .models import MegaBackgroundImage
from .models import EventBackgroundImage
from .models import NewsBackgroundImage
from .models import DonorBackgroundImage
from .models import ContributorBackgroundImage
from .models import ContentBackgroundImage
from .models import PartnerBackgroundImage
from .models import ShareBackgroundImage
from .models import WhyBackgroundImage
from .models import ProductBackgroundImage
from .models import SettingsModel
from .models import ImageCarousel
from .models import PostLikes
from .models import ConvertBackgroundImage
from .models import ReasonsBackgroundImage
from .models import SettingsBackgroundImage
from .models import PunishAppsBackgroundImage
from .models import BanAppealBackgroundImage
from .models import SupportBackgroundImage
from .models import OrderBackgroundImage
from .models import CheckoutBackgroundImage
from .models import SignupBackgroundImage
from .models import PerksBackgroundImage
from .models import ChangePasswordBackgroundImage
from .models import IssueBackgroundImage
from .models import BackgroundImageBase
from .models import TextBase
from .models import LogoBase
from .models import FrequentlyAskedQuestions
from .models import MemberHomeBackgroundImage
from .models import NavBar
from .models import NavBarHeader
from .models import FeaturedNavigationBar
from .models import DonateIcon
from .models import Donate
from .models import Titled
from .models import AdvertisementBase
from .models import ImageBase
from .models import SocialMedia
from .models import AdminRoles
from .models import AdminTasks
from .models import AdminPages
# from .models import Background2aImage
from .forms import PosteForm, EmailForm, AnswerForm, ItemForm, TradeItemForm, TradeProposalForm, SellerApplicationForm, \
    MemeForm, CurrencyCheckoutForm, CurrencyPaymentForm, CurrencyPaypalPaymentForm, HitStandForm, WagerForm, \
    DirectedTradeOfferForm, FriendRequestForm, RespondingTradeOfferForm, ShippingForm, EndowmentForm, UploadCardsForm, \
    RoomSettings, WithdrawForm, ExchangePrizesForm, AddTradeForm, GameForm, CardUploading, GameForm, MoveToTradeForm
from .forms import PostForm
from .forms import Postit
from .forms import StaffJoin
from .forms import Server_Partner
from .forms import SignUpForm
from .forms import News_Feed
from .forms import PunishAppeale
from .forms import ReportIssues
from .forms import BanAppeale
from .forms import Staffprofile
from .forms import Eventform
from .forms import ProfileDetail
from .forms import SupportForm
from .forms import SettingsForm
from .forms import BackgroundImagery
from .forms import EBackgroundImagery
from .forms import ShowcaseBackgroundImagery
from .forms import ChatBackgroundImagery
from .forms import BilletBackgroundImagery
from .forms import BlogBackgroundImagery
from .forms import PostBackgroundImagery
from .forms import RuleBackgroundImagery
from .forms import AboutBackgroundImagery
from .forms import FaqBackgroundImagery
from .forms import StaffBackgroundImagery
from .forms import InformationBackgroundImagery
from .forms import TagBackgroundImagery
from .forms import UserBackgroundImagery
from .forms import StaffRanksBackgroundImagery
from .forms import MegaBackgroundImagery
from .forms import EventBackgroundImagery
from .forms import NewsBackgroundImagery
from .forms import PaypalPaymentForm
from .forms import BaseCopyrightTextField
from .forms import ContactForme
from .forms import SignUpForm
from .forms import StoreViewTypeForm
# from .forms import OrderItems
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.db.models import Q
from django.views import generic
from django.views.generic import TemplateView, ListView

from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .forms import ProfileForm
from django.contrib.auth.models import User
from .models import Blog
from .models import BlogHeader
from .models import BlogFilter
from django.views.generic.edit import FormMixin

import pdb
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseNotFound, \
    HttpResponseBadRequest
from .forms import ContactForm
from .forms import BusinessContactForm
from .forms import BusinessMailingForm
from .forms import CommentForm
from django.shortcuts import get_object_or_404

from .models import Room, Message
from .models import SupportChat, SupportMessage
from .models import SupportLine
from .models import SupportInterface
from django.http import JsonResponse
import os

from django.contrib.auth.decorators import login_required

from guest_user.mixins import RegularUserRequiredMixin

from guest_user.decorators import allow_guest_user

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from datetime import datetime
from django.utils import timezone
from .forms import CheckoutForm
from .models import (Item, OrderItem, Order, Address, Payment, Coupon, Refund,
                     UserProfile)

from django.views.decorators.csrf import csrf_exempt

from django.views.generic.edit import FormView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SignupView(FormMixin, ListView):
    model = SignupBackgroundImage
    template_name = "cv-form.html"
    form_class = SignUpForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup'] = SignupBackgroundImage.objects.all()
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        return context

    def post(self, request, *args, **kwargs):
        print('signup')
        if request.method == 'POST':
            print('post')
            form = SignUpForm(request.POST)
            if form.is_valid():
                print('is_valid')
                user = form.save()
                user.refresh_from_db()
                # load the profile instance created by the signal
                user.save()
                raw_password = form.cleaned_data.get('password')

                # login user after signing up
                user = form.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                subject = "Welcome to IntelleX!"
                message = 'Hello {user.username}, thank you for becoming a member of the IntelleX Community!'
                email_from = settings.EMAIL_HOST_USER
                recipent_list = [user.email, ]
                send_mail(subject, message, email_from, recipent_list)

                # redirect user to home page
                return redirect('showcase:showcase')
                messages.info(request, "You have signed up successfully! Welcome!")
        else:
            form = SignUpForm()
        return render(request, 'cv-form.html', {'form': form})


class TotalView(ListView):
    model = BackgroundImageBase

    def _context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['TextFielde'] = TextBase.objects.filter(is_active=1).order_by("section")
        return context


class LogoView(ListView):
    model = LogoBase

    # ought to span multiple pages, not simply index

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Logo'] = LogoBase.objects.filter('page')
        return context


from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile

from .models import Advertising


class AdvertisementView(ListView):
    model = AdvertisementBase

    def display_advertisement(request, advertisement_id):
        advertising = Advertising.objects.get(id=advertising_id)
        context = {'advertising': advertising}
        return render(request, 'index.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Advertisement'] = AdvertisementBase.objects.filter(page=self.template_name, is_active=1)
        return context


"""    def handle_uploaded_image(i):
       # resize image
       imagefile  = StringIO.StringIO(i.read())
       imageImage = Image

       (width, height) = imageImage.size
       (width, height) = scale_dimensions(width, height, longest_side=240)

       resizedImage = imageImage.resize((width, height))

       imagefile = StringIO.StringIO()
       resizedImage.save(imagefile,'JPEG')"""


def set_image_position(image_id, xposition, yposition):
    # Retrieve the Image object from the database
    image = ImageBase.objects.get(id=image_id)
    print("Current coordinates: x={image.x}, y={image.y}")

    # Set the x and y positions to the desired values
    image.x = xposition
    image.y = yposition

    # Save the updated Image object back to the database
    image.save()


class ImageView(ListView):
    model = ImageBase

    def post(self, request, *args, **kwargs):
        # Get the image ID and new position values from the request
        image_id = request.POST.get('image_id')
        xposition = request.POST.get('xposition')
        yposition = request.POST.get('yposition')

        # Update the image position in the database
        set_image_position(image_id, xposition, yposition)

        # Render a response to the user
        return HttpResponse('Image position updated.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Image'] = ImageBase.objects.filter(page=self.template_name, is_active=1)
        return context


class BaseView(ListView):
    template_name = "base.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(is_active=1)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        user = self.request.user
        print(f'User: {user.username}, is_authenticated: {user.is_authenticated}, is_staff: {user.is_staff}')

        # Check if the user is an administrator and filter NavBarHeader accordingly
        if user.is_authenticated and user.is_staff:
            print('Staff is presently present')
            context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        else:
            # Filter NavBarHeader to exclude "admin" items
            print('User is not staff')
            context['Header'] = NavBarHeader.objects.filter(is_active=1).exclude(
                text__icontains="Admin"
            ).order_by("row")

            # Print the headers for debugging
            print('Headers:')
            for header in context['Header']:
                print(header.text)

        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        return context


class EBaseView(ListView):
    template_name = "ebase.html"
    model = NavBar

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        context = {}
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logos'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        return context


class BlogBaseView(ListView):
    template_name = "blogbase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['FeaturedNavigation'] = FeaturedNavigationBar.objects.filter(is_active=1).order_by("position")
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        return context


from .models import Preference


def detail_post_view(request, id=None):
    eachpost = get_object_or_404(Post, id=id)

    context = {'eachpost': eachpost}

    return render(request, 'showcase:likes.html', context)


@login_required
def postpreference(request, post_name, like_or_dislike):
    if request.method == "POST":
        eachpost = get_object_or_404(Blog, slug=post_name)

        if request.user in eachpost.likes.iterator():
            eachpost.likes.remove(request.user)
        if request.user in eachpost.dislikes.iterator():
            eachpost.dislikes.remove(request.user)

        if int(like_or_dislike) == 1:
            eachpost.likes.add(request.user)
        else:
            eachpost.dislikes.add(request.user)

        context = {'eachpost': eachpost,
                   'post_name': post_name}

        return render(request, 'likes.html', context)

    else:
        eachpost = get_object_or_404(Blog, slug=post_name)
        context = {'eachpost': eachpost,
                   'post_name': post_name}

        return render(request, 'showcase:likes.html', context)


# like is not connected to blog yet is used to filter

# id is used by this model but the blogpost uses slugs
from django.contrib.admin.views.decorators import staff_member_required
from django.views import View
from django.utils.decorators import method_decorator


@method_decorator(staff_member_required, name='dispatch')
class AdminRolesView(BaseView):
    template_name = "administrativeroles.html"
    model = AdminRoles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Roles'] = AdminRoles.objects.filter(is_active=1)
        return context


@method_decorator(staff_member_required, name='dispatch')
class AdminTasksView(ListView):
    template_name = "administrativetasks.html"
    model = AdminTasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Tasks'] = AdminTasks.objects.filter(is_active=1)
        return context


@method_decorator(staff_member_required, name='dispatch')
class AdminPagesView(ListView):
    template_name = "administrativepages.html"
    model = AdminPages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Pages'] = AdminPages.objects.filter(is_active=1)
        return context


@method_decorator(staff_member_required, name='dispatch')
class AdministrationView(ListView):
    template_name = "administration.html"
    model = AdminPages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Pages'] = AdminPages.objects.filter(is_active=1)
        context['Tasks'] = AdminTasks.objects.filter(is_active=1)
        return context


class DonateBaseView(ListView):
    template_name = "donatebase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        return context


class MemberBaseView(ListView):
    template_name = "memberbase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        return context


class usersview(ListView):
    paginate_by = 10
    template_name = 'users.html'

    def get_queryset(self):
        return Idea.objects.all()


"""
class PostList(BaseView):
    model = BlogBackgroundImage
    # backgroundqueryset = BackgroundImageBase.objects.filter('page').order_by('position')
    # queryset = Blog.objects.filter(status=1).order_by('-created_on')
    # normally can only filter once per view
    paginate_by = 10
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        print(124)
        context = super().get_context_data(**kwargs)
        context['BlogBackgroundImage'] = BlogBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['TextFielde'] = TextBase.objects.filter(is_active=1)
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['FeaturedNavigation'] = FeaturedNavigationBar.objects.filter(is_active=1).order_by("position")
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)

        # Retrieve the signed-in user's profile and profile picture URL

        # Retrieve the author's profile avatar
        blog_posts = Blog.objects.filter(status=1).order_by('-created_on')

        context['BlogPosts'] = blog_posts

        for blog_post in context['BlogPosts']:
            author = blog_post.author
            profile = ProfileDetails.objects.filter(user=author).first()
            if profile:
                blog_post.author_profile_picture_url = profile.avatar.url
                blog_post.author_profile_url = blog_post.get_profile_url()

                print('imgsrcimg')

        return context

    def get_queryset(self):
        return Blog.objects.filter(status=1).order_by('-created_on')

"""

"""
class votingview(ListView):
    model = VoteBackgroundImage
    paginate_by = 10
    template_name = 'voting.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Vote'] = Vote.objects.all()

        newprofile = Vote.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context

    def get_queryset(self):
        return Vote.objects.all()
"""


class partnerview(ListView):
    paginate_by = 10
    template_name = 'partners.html'

    def get_queryset(self):
        return PartnerApplication.objects.all()


class newsfeedview(ListView):
    paginate_by = 10
    template_name = 'newsfeed.html'

    def get_queryset(self):
        return NewsFeed.objects.all()


class Issueview(ListView):
    paginate_by = 10
    template_name = 'issues.html'

    def get_queryset(self):
        return ReportIssue.objects.all()


class staffview(ListView):
    paginate_by = 10
    template_name = 'staff.html'

    def get_queryset(self):
        return StaffProfile.objects.all()


class eventview(ListView):
    paginate_by = 10
    template_name = 'events.html'

    def get_queryset(self):
        return Event.objects.all()


class supportview(ListView):
    paginate_by = 10
    template_name = 'supportissues.html'

    def get_queryset(self):
        return Support.objects.all()


class MemberHomeBackgroundView(ListView):
    model = MemberHomeBackgroundImage
    template_name = "memberhome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['PatreonBackgroundImage'] = PatreonBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['MemberHomeBackgroundImage'] = MemberHomeBackgroundImage.objects.all()
        return context


class BusinessMessageBackgroundView(ListView):
    model = BusinessMessageBackgroundImage
    template_name = "businessemail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['PatreonBackgroundImage'] = PatreonBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BusinessMessageBackgroundImage'] = BusinessMessageBackgroundImage.objects.all()
        return context


class PatreonBackgroundView(ListView):
    model = Patreon
    template_name = "patreon.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['PatreonBackgroundImage'] = PatreonBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        # context['Patreon'] = Patreon.objects.all()
        return context


class BlogComment(generic.DetailView):
    model = Blog
    paginate_by = 10
    template_name = 'blog_comment.html'

    def post(self, request, slug, *args, **kwargs):
        most_recent = Blog.objects.order_by('-created_on')[:3]

        post = get_object_or_404(Blog, slug=slug)
        category_count = post.likes

        # if request.user.is_authenticated:
        #    BlogLikeView.objects.get_or_create(user=request.user, post=post)

        form = CommentForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                form.instance.user = request.user
                form.instance.post = post
                form.save()
                return redirect(reverse("blog_comment", kwargs={
                    'id': post.pk
                }))
        context = {
            'form': form,
            'post': post,
            'most_recent': most_recent,
            'category_count': category_count,
            'form': form
        }
        return render(request, 'blog_comment.html', context)


# def BlogPostLike(request, slug):
#    post = get_object_or_404(Blog, id=request.POST.get('blog_id'))
#    if post.likes.filter(id=request.user.id).exists():
#        post.likes.remove(request.user)
#    else:
#        post.likes.add(request.user)

#    return HttpResponseRedirect(reverse('showcase:post_detail', args=[str(slug)]))


# class BackgroundView(ListView):
#  paginate_by = 10
#  template_name = 'index.html'

#  def get_queryset(self):
#    return BackgroundImage.objects.all()

from django.views.generic import ListView, CreateView


# class TextFieldView(ListView):
#    model = TextField
#    template_name = "index.html"


class FaviconBaseView(ListView):
    model = FaviconBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Favicons'] = FaviconBase.objects.filter('faviconpage')
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        return context


class BackgroundBaseView(ListView):
    model = BackgroundImageBase

    # ought to span multiple pages, not simply index

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BackgroundImages'] = BackgroundImageBase.objects.filter('page').order_by('position')
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        return context

    # def backgrounds(request, showcase, index, blog):
    #    page = get_object_or_404(BackgroundImageBase,
    #                             showcase=showcase,
    #                             index=index,
    #                             blog=blog)

    # context = {
    #    'page': page,
    # }

    # if index == 'index':
    #    template = 'index.html'
    #    print(index)
    # elif index == 'showcase':
    #    template = 'showcase.html'
    #    print(index)
    # else render the one you're already rendering
    # else:
    #    template = 'blog.html'
    #    print(index)

    # return render(request, template, context)


class TextBaseView(ListView):
    model = TextBase

    # ought to span multiple pages, not simply index

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(is_active=1).order_by("section")
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        # texts = TextBase.objects.all()

        # if texts.exists():
        #    return JsonResponse({})
        # else:
        #    return context

        # def backgrounds(request, showcase, index, blog):
        #    page = get_object_or_404(BackgroundImageBase,
        #                             showcase=showcase,
        #                             index=index,
        #                             blog=blog)

        # context = {
        #    'page': page,
        # }

        # if index == 'index':
        #    template = 'index.html'
        #    print(index)
        # elif index == 'showcase':
        #    template = 'showcase.html'
        #    print(index)
        # else render the one you're already rendering
        # else:
        #    template = 'blog.html'
        #    print(index)

        return render(context)


class ImageCarouselView(BaseView):
    model = ImageCarousel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Carousel'] = ImageCarousel.objects.filter(is_active=1).order_by('position')
        return context


# class BackgroundView(FormMixin, BaseView):
#    model = BackgroundImage
#    form_class = EmailForm
#    template_name = "index.html"
#    section = TextBase.section

#    def post(self, request, *args, **kwargs):
#        form = EmailForm(request.POST)

#        if form.is_valid():
#            post = form.save(commit=False)
#            form.instance.user = request.user
#            post.save()
#            messages.success(request, 'Email subscription added!')
#            try:
#                email = EmailField.objects.get(user=request.user)
#                profile = ProfileDetails.objects.get(user=request.user)
#                profile.email = email.email
#                profile.save()
#            except ProfileDetails.DoesNotExist:
#                messages.error(request, 'Profile details not found.')
#            except EmailField.DoesNotExist:
#                print("EmailField does not exist.")
#            except Exception as e:
#                messages.error(request, f'An error occurred: {e}')
#            try:
#                email = EmailField.objects.get(user=request.user)
#                user = request.user
#                user.email = email.email
#                user.save()
#            except Exception as e:
#                messages.error(request, f'An error occurred: {e}')

#            return render(request, "emaildone.html", {'form': form})

#        else:
#            messages.error(request, "Form submission invalid")
#            print(form.errors)
#            print(form.non_field_errors())
#            print(form.cleaned_data)
#            return render(request, "index.html", {'form': form})
#            return redirect('showcase:index')

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
#        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
#        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
#        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
#        context['Carousel'] = ImageCarousel.objects.filter(is_active=1, carouselpage=self.template_name).order_by(
#            "carouselposition")
#        context['Advertisement'] = AdvertisementBase.objects.filter(page=self.template_name, is_active=1).order_by(
#            "advertisement_position")
#        context['Image'] = ImageBase.objects.filter(page=self.template_name, is_active=1).order_by("image_position")
#        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
#        context['Social'] = SocialMedia.objects.filter(page=self.template_name, is_active=1)
#        context['Feed'] = Feedback.objects.filter(is_active=1, feedbackpage=self.template_name).order_by("slug")
#        context['Email'] = EmailField.objects.filter(is_active=1)
#        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
#        context['Feedback'] = Feedback.objects.filter(showcase=1, is_active=1)
# context['Events'] = Event.objects.filter(page=self.template_name, is_active=1)
#        print(FaviconBase.objects.all())
#        print(213324)
#        # Retrieve the signed-in user's profile and profile picture URL

# Retrieve the items
#        product = Item.objects.filter(is_active=1)

#        context['Products'] = product

#        for product in context['Products']:
#            image = product.image
#            item = Item.objects.filter(slug=product.slug).first()
#            if product:
#                product.title = item.title
#                product.price = item.price
#                product.discount_price = item.discount_price
#                product.image_url = item.image.url
#                product.label = item.label
#                product.hyperlink = item.get_profile_url()
#                product.description = item.description

#        events = Event.objects.filter(is_active=1)
#        context['NewEvents'] = events

#        for events in context['NewEvents']:
#            image = events.image
#            eventful = Event.objects.filter(date_and_time=events.date_and_time).first()
#            if events:
#                events.name = eventful.name
#                events.image_url = eventful.image.url
#                events.hyperlink = eventful.get_profile_url()
#                events.description = eventful.description

#        context['News'] = NewsFeed.objects.all()

#        newprofile = NewsFeed.objects.filter(is_active=1)
# Retrieve the author's profile avatar

#        context['Profiles'] = newprofile

#        for newprofile in context['Profiles']:
#            user = newprofile.user
#            profile = ProfileDetails.objects.filter(user=user).first()
#            if profile:
#                newprofile.newprofile_profile_picture_url = profile.avatar.url
#                newprofile.newprofile_profile_url = newprofile.get_profile_url()

#        feedback_objects = Feedback.objects.filter(slug=slug)

# Add the feedback_objects to the context
#        context['Feed'] = feedback_objects

#        for feedback_objects in context['Feed']:
#            user = feedback_objects.username
#            profile = ProfileDetails.objects.filter(user=user).first()
#            if profile:
#                feedback_objects.newprofile_profile_picture_url = profile.avatar.url
#                feedback_objects.newprofile_profile_url = feedback_objects.get_profile_url2()

#        return context


from django.views.generic import TemplateView
from .models import BackgroundImage


class BackgroundStyleView(TemplateView):
    template_name = "style.css"
    content_type = "text/css"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the first BackgroundImage object from the database
        background_image = BackgroundImageBase.objects.first()
        # Add it to the context with the name 'BackgroundImage'
        context['Background'] = background_image
        return context


def dynamic_css(request):
    background_objects = BackgroundImageBase.objects.filter(page='index').order_by("position")

    context = {
        'background_objects': background_objects,
    }

    return render(request, 'dynamic_css.css', context, content_type='text/css')


class CreatePostView(CreateView):
    model = BackgroundImage
    form_class = BackgroundImagery
    template_name = "backgroundimagechange.html"
    success_url = reverse_lazy("index")


class ECreatePostView(CreateView):
    model = EBackgroundImage
    form_class = EBackgroundImagery
    template_name = "ebackgroundimagechange.html"
    success_url = reverse_lazy("ehome")


class ShowcaseBackgroundView(BaseView):
    model = ShowcaseBackgroundImage
    template_name = "showcase.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ShowcaseBackgroundImage'] = ShowcaseBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['UpdateProfile'] = UpdateProfile.objects.all()

        newprofile = UpdateProfile.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class ShowcaseCreatePostView(CreateView):
    model = ShowcaseBackgroundImage
    form_class = ShowcaseBackgroundImagery
    template_name = "showcasebackgroundimagechange.html"
    success_url = reverse_lazy("showcase")


def create_responding_tradeoffer(request, tradeoffer_pk):
    related_offer = TradeOffer.objects.get(pk=tradeoffer_pk)
    if request.method == 'POST':
        form = RespondingTradeOfferForm(request.POST, related_offer=related_offer)
        if form.is_valid():
            form.save()
            # Handle successful form submission
    else:
        form = RespondingTradeOfferForm(related_offer=related_offer)
    return render(request, 'tradingcentral.html', {'form': form})


class ChatBackgroundView(BaseView):
    model = ChatBackgroundImage
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Friends'] = Friend.objects.filter(user=self.request.user)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)

        current_user = self.request.user
        newprofile = UserProfile2.objects.filter(is_active=1, user=current_user)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        onlineprofile = Friend.objects.filter(is_active=1, user=current_user)

        context['OnlineProfiles'] = onlineprofile

        for onlineprofile in context['OnlineProfiles']:
            friend = onlineprofile.friend
            activeprofile = ProfileDetails.objects.filter(user=friend).first()
            if activeprofile:
                onlineprofile.author_profile_picture_url = profile.avatar.url
                onlineprofile.friend_profile_picture_url = activeprofile.avatar.url
                onlineprofile.author_profile_url = onlineprofile.get_profile_url()
                onlineprofile.friend_name = onlineprofile.friend.username
                print('activeprofile exists')

        friends = Friend.objects.filter(user=self.request.user)

        # Prepare a list to hold the friends' data
        friends_data = []

        for friend in friends:
            # Get the friend's profile
            profile = ProfileDetails.objects.filter(user=friend.friend).first()

            if profile:
                # Add the friend's data to the list
                friends_data.append({
                    'username': friend.friend.username,
                    'profile_picture_url': profile.avatar.url,
                    'profile_url': reverse('showcase:profile', args=[str(profile.pk)]),
                    'currently_active': friend.currently_active,
                    'user_profile_url' : friend.get_profile_url2()
                })

        # Add the friends' data to the context
        context['friends_data'] = friends_data

        search_term = self.request.GET.get('search', '')
        if search_term:
            context = self.search_friends(context)  # Call search_friends if search term exists

        return context

    def search_friends(self, context):
        search_term = self.request.GET.get('search', '')
        if search_term:
            item_list = Friend.objects.filter(
                Q(friend__username__icontains=search_term)
            ).prefetch_related('friend')  # Prefetch the friend object

            # Prepare a list to hold the searched friends' data
            search_results_data = []
            current_user = self.request.user

            for friend in item_list:

                profile = ProfileDetails.objects.filter(user=friend.friend).first()

                if profile:
                    search_results_data.append({
                        'username': friend.friend.username,
                        'profile_picture_url': profile.avatar.url if profile else None,
                        # Handle cases where profile might be missing
                        'profile_url': reverse('showcase:profile', args=[str(profile.pk)]),
                        'currently_active': friend.currently_active,
                    })
                    print('the friend does have a profile')
                else:
                    # Handle cases where profile details might be missing (optional)
                    search_results_data.append({
                        'username': friend.friend.username,
                        'profile_picture_url': None,  # Set to None or a default image URL
                        'profile_url': reverse('showcase:profile', args=[str(friend.friend.pk)]),
                        'currently_active': friend.currently_active,
                    })
                    print('no profile on the friend')

            context['search_results'] = search_results_data  # Update context with search results data
        else:
            context['search_results'] = []  # Empty list if no search

        return context


from django.views.generic import ListView


class FriendSearchResultsView(ListView):
    model = Friend
    template_name = 'friendssearchresultview.html'

    def get_queryset(self):
        search_term = self.request.GET.get('search', '')  # Get the search term (default empty string)
        if search_term:
            item_list = Friend.objects.filter(
                Q(friend_username__icontains=search_term)  # Filter on friend's username
            )
            print('item_list contains' + str(item_list))
        else:
            item_list = Friend.objects.none()  # Return an empty queryset if no search term
            print('item_list is empty')
        return item_list

from django.shortcuts import render

def friendlysearchresultview(request):
  search_term = request.GET.get('search', '')
  if search_term:
    item_list = Friend.objects.filter(
        Q(friend__username__icontains=search_term)
    )
  else:
    item_list = Friend.objects.none()
  context = {'item_list': item_list}  # Add item_list to context
  return render(request, 'friendssearchresultview.html', context)  # Render the template


class SupportChatBackgroundView(BaseView):
    model = SupportChatBackgroundImage
    template_name = "supportchat.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        return context


class PlaceWagerView(FormView):
    template_name = 'template_name.html'
    form_class = WagerForm
    success_url = reverse_lazy('showcase')  # replace with your actual view name

    def form_valid(self, form):
        wager = form.save(commit=False)
        wager.user_profile = self.request.user.userprofile
        wager.save()
        return super().form_valid(form)


from django.core.exceptions import ValidationError


@csrf_exempt
def update_wager(request, wager_id):
    if request.method == 'POST':
        outcome = request.POST.get('outcome')
        wager = get_object_or_404(Wager, pk=wager_id)

        # Validate the outcome
        valid_outcomes = ('W', 'L', 'D', 'B')  # Replace with your model choices
        if outcome not in valid_outcomes:
            raise ValidationError("Invalid outcome submitted")

        wager.outcome = outcome
        wager.save()

        # Optionally return a JSON response with success message
        return JsonResponse({'success': True, 'message': 'Wager updated successfully'})

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class ChestBackgroundView(BaseView):
    model = UserProfile
    template_name = "blackjack.html"

    def post(self, request, *args, **kwargs):
        form = WagerForm(request.POST, user_profile=request.user.user_profile)
        if form.is_valid():
            wager = form.save(commit=False)
            wager.user_profile = request.user.user_profile
            wager.save()
            # Return the wager id to the client
            return JsonResponse({'wager_id': wager.id})
        else:
            # If the form is not valid, re-render the page with the form errors
            return self.get(request, *args, **kwargs)

    @csrf_exempt  # Handle CSRF if needed
    def update_wager(request):
        if request.method == 'POST':
            wager_id = request.POST.get('wager_id')
            outcome = request.POST.get('outcome')
            try:
                wager = Wager.objects.get(id=wager_id)
                wager.resolve(outcome)
                return JsonResponse({'status': 'success'})
            except Wager.DoesNotExist:
                return JsonResponse({'error': 'Wager not found.'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Invalid request method.'}, status=405)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ShowcaseBackgroundImage'] = ShowcaseBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['wager_form'] = WagerForm()

        newprofile = UpdateProfile.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class PokeChestBackgroundView(BaseView):
    model = UserProfile
    template_name = "pokechests.html"

    def post(self, request, *args, **kwargs):
        form = WagerForm(request.POST, user_profile=request.user.user_profile)
        if form.is_valid():
            wager = form.save(commit=False)
            wager.user_profile = request.user.user_profile
            wager.save()
            return redirect('showcase:blackjack')  # replace with your actual view name
        else:
            # If the form is not valid, re-render the page with the form errors
            return self.get(request, *args, **kwargs)

    @csrf_exempt  # Handle CSRF if needed
    def update_wager(request):
        if request.method == 'POST':
            wager_id = request.POST.get('wager_id')
            outcome = request.POST.get('outcome')
            try:
                wager = Wager.objects.get(id=wager_id)
                wager.resolve(outcome)
                return JsonResponse({'status': 'success'})
            except Wager.DoesNotExist:
                return JsonResponse({'error': 'Wager not found.'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Invalid request method.'}, status=405)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ShowcaseBackgroundImage'] = ShowcaseBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['games'] = Game.objects.filter(is_active=1)  # Queryset of active games
        context['wager_form'] = WagerForm()

        newprofile = UpdateProfile.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


def find_choice(request):
    # Generate a random nonce between 0 and 1000000
    generated_nonce = random.randint(0, 1000000)

    # Query the Choice model to find the choice that includes the generated nonce
    choice = Choice.objects.filter(lower_nonce__lte=generated_nonce, upper_nonce__gte=generated_nonce).first()

    # Pass the generated nonce and the found choice to the template
    context = {
        'generated_nonce': generated_nonce,
        'choice': choice
    }

    return render(request, 'choice_detail.html', context)


class FindChoiceView(View):
    template_name = 'choice_detail.html'

    def get(self, request, *args, **kwargs):
        # Generate a random nonce between 0 and 1000000
        generated_nonce = random.randint(0, 1000000)

        # Query the Choice model to find the choice that includes the generated nonce
        choice = Choice.objects.filter(lower_nonce__lte=generated_nonce, upper_nonce__gte=generated_nonce).first()

        # Pass the generated nonce and the found choice to the template
        context = {
            'generated_nonce': generated_nonce,
            'choice': choice
        }

        return render(request, self.template_name, context)


def game_view(request, slug):
    game = get_object_or_404(Game, slug=slug)
    outcome = Outcome()
    if request.method == 'POST':
        nonces = [random.randint(0, 1000000) for _ in range(3)]

        # Retrieve the game
        game = Game.objects.get(id=game_id)

        # Find the choices that match the nonces
        matching_choices = []
        for nonce in nonces:
            choices = Choice.objects.filter(lower_nonce__lte=nonce, upper_nonce__gte=nonce, game=game)
            for choice in choices:
                matching_choices.append((nonce, choice))

        # Randomize the order of choices
        random.shuffle(matching_choices)

        # Prepare data to return as JSON
        choices_data = [{
            'nonce': nonce,
            'choice_text': choice.choice_text,
            'value': choice.value,
            'file_url': choice.file.url
        } for nonce, choice in matching_choices]

        return JsonResponse({
            'status': 'success',
            'choices': choices_data
        })
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def create_outcome(request, slug):
    if request.method == 'POST':
        print("Received a POST request")
        game_id = request.POST.get('game_id')
        user = request.user

        print(f"Received POST request with game_id: {game_id}")

        if not game_id:
            print("Game ID is missing.")
            return JsonResponse({'status': 'error', 'message': 'Game ID is required.'})

        try:
            game = Game.objects.get(id=game_id, slug=slug)
            nonce = random.randint(1, 1000000)
            choices = Choice.objects.filter(lower_nonce__lte=nonce, upper_nonce__gte=nonce)

            if not choices.exists():
                print(f"No choice found for nonce {nonce}.")
                return JsonResponse({'status': 'error', 'message': 'No valid choice found for the given nonce.'})

            choice = choices.order_by('?').first()  # Select a random choice if multiple choices are found

            outcome = Outcome.objects.create(
                user=user,
                game=game,
                choice=choice,
                nonce=nonce,
                value=random.randint(1, 1000000),  # example value, adjust as needed
                ratio=random.randint(1, 10)    # example ratio, adjust as needed
            )
            print(f"Created outcome with nonce: {outcome.nonce}")
            return JsonResponse({'status': 'success', 'outcome': outcome.id, 'nonce': outcome.nonce})
        except Game.DoesNotExist:
            print("Game not found.")
            return JsonResponse({'status': 'error', 'message': 'Game not found.'})
        except Exception as e:
            print(f"Exception: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def game_view(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    # Use the discount cost if available, otherwise use the regular cost
    cost = game.discount_cost if game.discount_cost else game.cost

    context = {
        'game': game,
        'cost_threshold_80': cost * 0.8,
        'cost_threshold_100': cost,
        'cost_threshold_200': cost * 2,
        'cost_threshold_500': cost * 5,
        'cost_threshold_10000': cost * 100,
    }

    return render(request, 'game.html', context)


class GameChestBackgroundView(TemplateView):
    model = UserProfile
    template_name = "game.html"

    def post(self, request, *args, **kwargs):
        form = WagerForm(request.POST, user_profile=request.user.user_profile)
        if form.is_valid():
            wager = form.save(commit=False)
            wager.user_profile = request.user.user_profile
            wager.save()
            return redirect('showcase:blackjack')  # replace with your actual view name
        else:
            # If the form is not valid, re-render the page with the form errors
            return self.get(request, *args, **kwargs)

    @csrf_exempt
    def create_outcome(request):
        if request.method == 'POST':
            game_id = request.POST.get('game_id')
            choice_id = request.POST.get('choice_id')
            user = request.user

            print(f"Received POST request with game_id: {game_id} and choice_id: {choice_id}")

            if not game_id or not choice_id:
                return JsonResponse({'status': 'error', 'message': 'Game ID and Choice ID are required.'})

            try:
                game = Game.objects.get(id=game_id)
                choice = Choice.objects.get(id=choice_id)
                nonce = random.randint(0, 1000000)
                outcome = Outcome.objects.create(
                    user=user,
                    game=game,
                    choice=choice,
                    nonce=nonce,
                    value=random.randint(1, 100),  # example value, adjust as needed
                    ratio=random.randint(1, 10)  # example ratio, adjust as needed
                )
                print(f"Created outcome with nonce: {outcome.nonce}")
                return JsonResponse({'status': 'success', 'nonce': outcome.nonce})
            except Game.DoesNotExist:
                print("Game not found.")
                return JsonResponse({'status': 'error', 'message': 'Game not found.'})
            except Choice.DoesNotExist:
                print("Choice not found.")
                return JsonResponse({'status': 'error', 'message': 'Choice not found.'})
            except Exception as e:
                print(f"Exception: {str(e)}")
                return JsonResponse({'status': 'error', 'message': str(e)})

        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

    @csrf_exempt  # Handle CSRF if needed
    def update_wager(request):
        if request.method == 'POST':
            wager_id = request.POST.get('wager_id')
            outcome = request.POST.get('outcome')
            try:
                wager = Wager.objects.get(id=wager_id)
                wager.resolve(outcome)
                return JsonResponse({'status': 'success'})
            except Wager.DoesNotExist:
                return JsonResponse({'error': 'Wager not found.'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Invalid request method.'}, status=405)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['games'] = Game.objects.filter(is_active=1, slug=slug)  # Filter games by slug
        context['wager_form'] = WagerForm()
        game = get_object_or_404(Game, slug=slug)

        cost = game.discount_cost if game.discount_cost else game.cost

        context.update({
            'game': game,
            'cost_threshold_80': cost * 0.8,
            'cost_threshold_100': cost,
            'cost_threshold_200': cost * 2,
            'cost_threshold_500': cost * 5,
            'cost_threshold_10000': cost * 100,
        })
        newprofile = UpdateProfile.objects.filter(is_active=1)
        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class ChatCreatePostView(CreateView):
    model = ChatBackgroundImage
    form_class = ChatBackgroundImagery
    template_name = "chatbackgroundimagechange.html"
    success_url = reverse_lazy("home")


class WhyBackgroundView(BaseView):
    model = WhyBackgroundImage
    template_name = "whydonate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        return context


class GameHubView(BaseView):
    model = GameHub
    template_name = "gamehub.html"

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:emaildone')
        else:
            messages.error(request, "Form submission invalid")
            print("there was an error in registering the email")
            return render(request, "gamehub.html", {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ShowcaseBackgroundImage'] = ShowcaseBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['Game'] = GameHub.objects.filter(is_active=1)
        context['form'] = EmailForm()

        return context


class GameRoomView(BaseView):
    model = GameHub
    template_name = "gameroom.html"

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:emaildone')
        else:
            messages.error(request, "Form submission invalid")
            print("there was an error in registering the email")
            return render(request, "gameroom.html", {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ShowcaseBackgroundImage'] = ShowcaseBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['Game'] = GameHub.objects.filter(is_active=1).first()
        context['GameRoom'] = Game.objects.filter(is_active=1).first()
        context['form'] = EmailForm()

        newprofile = Game.objects.filter(is_active=1)
        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class ClubRoomView(BaseView):
    model = GameHub
    template_name = "clubroom.html"

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:emaildone')
        else:
            messages.error(request, "Form submission invalid")
            print("there was an error in registering the email")
            return render(request, "blog.html", {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ShowcaseBackgroundImage'] = ShowcaseBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
        context['Money'] = Currency.objects.filter(is_active=1).first()
        context['Game'] = GameHub.objects.filter(is_active=1).first()
        context['form'] = EmailForm()

        newprofile = UpdateProfile.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class BlogBackgroundView(ListView):
    model = BlogBackgroundImage
    template_name = "blog.html"

    queryset = Blog.objects.filter(status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['BlogBackgroundImage'] = BlogBackgroundImage.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        return context


class BlogCreatePostView(CreateView):
    model = BlogBackgroundImage
    form_class = BlogBackgroundImagery
    template_name = "blogbackgroundimagechange.html"
    success_url = reverse_lazy("blog")


# @login_required
# @RegularUserRequiredMixin
class PostBackgroundView(FormMixin, LoginRequiredMixin, ListView):
    model = UpdateProfile
    template_name = "post_edit.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        return context

    # @login_required
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:showcase')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "post_edit.html", {'form': form})


class ShufflerBackgroundView(BaseView):
    model = Shuffler
    template_name = "pack_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ShowcaseBackgroundImage'] = ShowcaseBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['UpdateProfile'] = UpdateProfile.objects.all()
        context['Shuffle'] = Shuffler.objects.filter(is_active=1).order_by("category")

        newprofile = UpdateProfile.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class PostCreatePostView(CreateView):
    model = PostBackgroundImage
    form_class = PostBackgroundImagery
    template_name = "postbackgroundimagechange.html"
    success_url = reverse_lazy("post_edit")


class BilletBackgroundView(BaseView):
    model = BilletBackgroundImage
    template_name = "billets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['BilletBackgroundImage'] = BilletBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        return context


class BilletCreatePostView(CreateView):
    model = BilletBackgroundImage
    form_class = BilletBackgroundImagery
    template_name = "billetbackgroundimagechange.html"
    success_url = reverse_lazy("billets")


class RuleBackgroundView(BaseView):
    model = RuleBackgroundImage
    template_name = "rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Rules'] = RuleBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        return context


class RuleCreatePostView(CreateView):
    model = RuleBackgroundImage
    form_class = RuleBackgroundImagery
    template_name = "rulebackgroundimagechange.html"
    success_url = reverse_lazy("rules")


class PolicyBackgroundView(BaseView):
    template_name = "policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        return context


class ServersView(BaseView):
    model = RuleBackgroundImage
    template_name = "servers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        return context


class AboutCreatePostView(CreateView):
    model = AboutBackgroundImage
    form_class = AboutBackgroundImagery
    template_name = "aboutbackgroundimagechange.html"
    success_url = reverse_lazy("about")


class FaqBackgroundView(BaseView):
    model = FaqBackgroundImage
    template_name = "faq.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['FaqBackgroundImage'] = FaqBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        return context


class FaqCreatePostView(CreateView):
    model = FaqBackgroundImage
    form_class = FaqBackgroundImagery
    template_name = "faqbackgroundimagechange.html"
    success_url = reverse_lazy("faq")


class StaffBackgroundView(BaseView):
    model = BackgroundImage
    template_name = "staff.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        return context


class StaffCreatePostView(CreateView):
    model = StaffBackgroundImage
    form_class = StaffBackgroundImagery
    template_name = "staffbackgroundimagechange.html"
    success_url = reverse_lazy("staff")


class StaffApplyBackgroundView(FormMixin, ListView):
    model = StaffApplyBackgroundImage
    template_name = "staffapplications.html"
    form_class = StaffJoin

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['StaffApplyBackgroundImage'] = StaffApplyBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = StaffJoin(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:staffdone')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "staffapplications.html", {'form': form})
        else:
            form = StaffJoin()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "staffapplications.html", {'form': form})


class InformationBackgroundView(BaseView):
    InformationBackgroundImage
    template_name = "information.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context


class InformationCreatePostView(CreateView):
    model = InformationBackgroundImage
    form_class = InformationBackgroundImagery
    template_name = "Informationbackgroundimagechange.html"
    success_url = reverse_lazy("Information")


class TagBackgroundView(BaseView):
    model = TagBackgroundImage
    template_name = "tag.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        return context


class TagCreatePostView(CreateView):
    model = TagBackgroundImage
    form_class = TagBackgroundImagery
    template_name = "tagbackgroundimagechange.html"
    success_url = reverse_lazy("tag")


class UserBackgroundView(BaseView):
    model = UserBackgroundImage
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['UserBackgroundImage'] = UserBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context


class UserCreatePostView(CreateView):
    model = UserBackgroundImage
    form_class = UserBackgroundImagery
    template_name = "userbackgroundimagechange.html"
    success_url = reverse_lazy("users")


class StaffRanksBackgroundView(BaseView):
    model = StaffRanksBackgroundImage
    template_name = "staffranks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['StaffRanksBackgroundImage'] = StaffRanksBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context


class StaffRanksCreatePostView(CreateView):
    model = StaffRanksBackgroundImage
    form_class = StaffRanksBackgroundImagery
    template_name = "staffranksbackgroundimagechange.html"
    success_url = reverse_lazy("staffranks")


class MegaBackgroundView(BaseView):
    model = MegaBackgroundImage
    template_name = "megacoins.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MegaCoinsBackgroundImage'] = MegaBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context


class MegaCreatePostView(CreateView):
    model = MegaBackgroundImage
    form_class = MegaBackgroundImagery
    template_name = "megacoinsbackgroundimagechange.html"
    success_url = reverse_lazy("megacoins")


class EventBackgroundView(BaseView):
    model = EventBackgroundImage
    template_name = "events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['EventBackgroundImage'] = EventBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Events'] = Event.objects.all()

        newprofile = Event.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class EventCreatePostView(CreateView):
    model = EventBackgroundImage
    form_class = EventBackgroundImagery
    template_name = "eventbackgroundimagechange.html"
    success_url = reverse_lazy("event")


class NewsBackgroundView(BaseView):
    model = NewsBackgroundImage
    template_name = "newsfeed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['NewsBackgroundImage'] = NewsBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['News'] = NewsFeed.objects.all()

        newprofile = NewsFeed.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class SingleNewsView(DetailView):
    model = NewsFeed
    paginate_by = 10
    template_name = "singlenews.html"

    def get_object(self):
        slug = self.kwargs.get("slug")  # Get slug from URL parameters
        if slug:
            return get_object_or_404(NewsFeed, slug=slug)  # Retrieve profile or raise 404 for invalid slug
        return None  # Handle case where no slug is provided (optional

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['NewsBackgroundImage'] = NewsBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['News'] = NewsFeed.objects.all()

        newprofile = NewsFeed.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class NewsCreatePostView(CreateView):
    model = NewsBackgroundImage
    form_class = NewsBackgroundImagery
    template_name = "newsbackgroundimagechange.html"
    success_url = reverse_lazy("newsfeed")


class DonorView(BaseView):
    model = DonorBackgroundImage
    template_name = "donors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        # context['BaseHomeTexted'] = BaseHomeText.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context

    def dispatch(self, request, *args, **kwargs):
        # Check if there is a signed-in user
        if request.user.is_authenticated:
            user = request.user
            print(user)
        else:
            # If no signed-in user, use a default user or None as desired
            user = None  # Or use default_user if it is previously defined

        # Continue with the regular flow, passing the determined user to the view
        return super().dispatch(request, *args, user=user, **kwargs)


class ContributorBackgroundView(BaseView):
    model = ContributorBackgroundImage
    template_name = "contributors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        return context


class ContentBackgroundView(BaseView):
    model = ContentBackgroundImage
    template_name = "morecontent.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ContentBackgroundImage'] = ContentBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context


class PartnerApplicationView(FormMixin, LoginRequiredMixin, ListView):
    model = PartnerApplication
    template_name = "partnerapplication.html"
    form_class = Server_Partner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        return context

    # @login_required
    def post(self, request, *args, **kwargs):
        form = Server_Partner(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:partners')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "partnerapplication.html", {'form': form})




class PartnerBackgroundView(BaseView):
    model = PartnerBackgroundImage
    template_name = "partners.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['PartnerBackgroundImage'] = PartnerBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Partner'] = PartnerApplication.objects.all()

        newprofile = Partner.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class ConvertBackgroundView(BaseView):
    model = ConvertBackgroundImage
    template_name = "convert.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ConvertBackgroundImage'] = ConvertBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        return context


class ReasonsBackgroundView(BaseView):
    model = ReasonsBackgroundImage
    template_name = "reasons-to-convert.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ConvertBackgroundImage'] = ConvertBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        return context


class PerksBackgroundView(BaseView):
    model = PerksBackgroundImage
    template_name = "perks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ShowcaseBackgroundImage'] = ShowcaseBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['TextFielde'] = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")
        return context


#  def get_queryset(self):
#    return BackgroundImage.objects.all()

#  def get_context_data(request):
#    images = os.listdir("static/css/images") #Can use glob as well
#    context = {'images': images}
#    return render(request,'/home/runner/PokeTrove-Attempt-Backedmore/templates',context)

# class Background2aView(ListView):
#  model = Background2aImage
#  paginate_by = 10
#  template_name = 'index.html'
#  extra_context = {'Background2aIm
#  age.url': Background2aImage.objects.all()[0].get_absolute_url()}

#  def get_queryset(self):
#    return Background2aImage.objects.all()


def home(request):
    return render(request, 'home.html')


from django.http import HttpRequest, JsonResponse
from django.views.generic import TemplateView


class RoomView(TemplateView):
    model = Room
    template_name = 'room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        room_name = self.kwargs['room']  # assuming 'room' is the room name passed in the URL
        rooms_with_logo_same_name = Room.objects.filter(name=room_name).exclude(logo='')
        context['rooms_with_logo_same_name'] = rooms_with_logo_same_name
        room = self.kwargs['room']

        username = self.request.GET.get('username')
        room_details = Room.objects.get(name=room)
        profile_details = ProfileDetails.objects.filter(user__username=username).first()
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['username'] = username
        context['room_details'] = room_details
        context['profile_details'] = profile_details

        # Retrieve the author's profile avatar
        messages = Message.objects.all().order_by('-date')

        context['Messaging'] = messages

        for messages in context['Messaging']:
            profile = ProfileDetails.objects.filter(user=messages.signed_in_user).first()
            if profile:
                messages.user_profile_picture_url = profile.avatar.url
                messages.user_profile_url = messages.get_profile_url()

        current_user = self.request.user
        newprofile = UserProfile2.objects.filter(is_active=1, user=current_user)

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        onlineprofile = Friend.objects.filter(is_active=1, user=current_user).order_by('-last_messaged')
        current_highlighted_profile = Friend.objects.filter(is_active=1, user=current_user)

        context['OnlineProfiles'] = onlineprofile
        context['CurrentProfiles'] = current_highlighted_profile

        for onlineprofile in context['OnlineProfiles']:
            friend = onlineprofile.friend
            activeprofile = ProfileDetails.objects.filter(user=friend).first()
            if activeprofile:
                onlineprofile.author_profile_picture_url = profile.avatar.url
                onlineprofile.author_profile_url = onlineprofile.get_profile_url()
                onlineprofile.friend_profile_picture_url = profile.avatar.url
                onlineprofile.friend_profile_picture_url = onlineprofile.get_profile_url()
                onlineprofile.friend_name = onlineprofile.friend.username
                print('activeprofile exists')


        # Retrieve the author's profile avatar
        blog_posts = Blog.objects.filter(status=1).order_by('-created_on')

        context['BlogPosts'] = blog_posts

        for onlineprofile in context['CurrentProfiles']:
            friend = onlineprofile.friend
            activeprofile = ProfileDetails.objects.filter(user=friend).first()
            if activeprofile:
                onlineprofile.author_profile_picture_url = profile.avatar.url
                onlineprofile.friend_profile_picture_url = profile.avatar.url  # Add this line
                onlineprofile.author_profile_url = onlineprofile.get_profile_url()
                onlineprofile.friend_name = onlineprofile.friend.username
                print('currentfriendprofile exists')

        friends = Friend.objects.filter(user=self.request.user).order_by('last_messaged')

        # Prepare a list to hold the friends' data
        friends_data = []

        for friend in friends:
            # Get the friend's profile
            profile = ProfileDetails.objects.filter(user=friend.friend).first()
            friend_pk = self.request.GET.get('friend_pk')

            if profile:
                # Add the friend's data to the list
                friends_data.append({
                    'username': friend.friend.username,
                    'profile_picture_url': profile.avatar.url,
                    'profile_url': reverse('showcase:profile', args=[str(profile.pk)]),
                    'currently_active': friend.currently_active,
                    'user_profile_url' : friend.get_profile_url2()
                })
            if friend_pk and int(friend_pk) == friend.pk:  # Check if PK matches
                print('setting currently active')
                friend.currently_active = True
                friend.save()  # Update the friend's currently_active field
                return redirect('showcase:room', room=room)  # Redirect back to the room URL

        # Add the friends' data to the context
        context['friends_data'] = friends_data

        search_term = self.request.GET.get('search', '')
        if search_term:
            context = self.search_friends(context)  # Call search_friends if search term exists

        return context

    def search_friends(self, context):
        search_term = self.request.GET.get('search', '')
        if search_term:
            item_list = Friend.objects.filter(
                Q(friend__username__icontains=search_term)
            ).prefetch_related('friend')  # Prefetch the friend object

            # Prepare a list to hold the searched friends' data
            search_results_data = []
            current_user = self.request.user

            for friend in item_list:

                profile = ProfileDetails.objects.filter(user=friend.friend).first()

                if profile:
                    search_results_data.append({
                        'username': friend.friend.username,
                        'profile_picture_url': profile.avatar.url if profile else None,
                        # Handle cases where profile might be missing
                        'profile_url': reverse('showcase:profile', args=[str(profile.pk)]),
                    })
                    print('the friend does have a profile')
                else:
                    # Handle cases where profile details might be missing (optional)
                    search_results_data.append({
                        'username': friend.friend.username,
                        'profile_picture_url': None,  # Set to None or a default image URL
                        'profile_url': reverse('showcase:profile', args=[str(friend.friend.pk)]),
                    })
                    print('no profile on the friend')

            context['search_results'] = search_results_data  # Update context with search results data
        else:
            context['search_results'] = []  # Empty list if no search

        return context


def room(request, room):
    username = request.GET.get('username')

    profile_details = ProfileDetails.objects.filter(user__username=username).first()
    Logo = LogoBase.objects.filter(page='room.html', is_active=1)
    Header = NavBarHeader.objects.filter(is_active=1).order_by("row")
    DropDown = NavBar.objects.filter(is_active=1).order_by('position')

    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'signed_in_user': signed_in_user,
        'room_details': room_details,
        'profile_details': profile_details,
        'Logo': Logo,
        'Header': Header,
        'Dropdown': DropDown,
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    request.session['room_name'] = room
    request.session['username'] = username

    # Check if room exists in the database
    if Room.objects.filter(name=room).exists():
        return redirect('/home/' + room + '/?username=' + username)
    else:
        # Create room and assign user if authenticated
        new_room = Room.objects.create(name=room)
        signed_in_user = request.user
        print('the room owner is ' + str(signed_in_user))
        new_room.signed_in_user = signed_in_user if signed_in_user.is_authenticated else None
        new_room.save()
        # Redirect to create_room page after successful creation (assuming it exists)
        return redirect('showcase:create_room')  # Assuming you have a URL pattern named 'create_room'


def send(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        username = request.POST.get('username')
        room_id = request.POST.get('room_name')  # Get the room name from the POST request
        page_name = request.POST.get('page_name')

        if page_name == 'index.html':
            room_id = 'General'

        print(f"message: {message}, username: {username}, room_id: {room_id}, page_name: {page_name}")
        print('This is a community-sent message')

        if request.user.is_authenticated:
            new_message = Message.objects.create(
                value=message,
                user=username,
                room=Room.objects.get(name=room_id),  # Assign the room object to the room field
                signed_in_user=request.user
            )
        else:
            new_message = Message.objects.create(
                value=message,
                user=username,
                room=Room.objects.get(name=room_id)  # Assign the room object to the room field
            )
        # Return a success response
        return HttpResponse('Message sent successfully')

    # Handle invalid request methods
    return HttpResponse('Invalid request method. Please use POST to send a message.')

from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import JsonResponse
from django.views import View
from django.core import serializers

"""
def get_profile_url(message):
   return f"http://127.0.0.1:8000/profile/{message.signed_in_user_id}/"
"""
from django.http import JsonResponse


class NewRoomSettingsView(LoginRequiredMixin, TemplateView):
    template_name = "create_room.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_name = self.request.session.get('room_name')
        username = self.request.session.get('username')

        room = Room.objects.filter(name=room_name).first()
        form = RoomSettings(instance=room)  # replace with your actual form class

        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['form'] = form
        context['room'] = room
        # add other context variables as needed

        return context

    def post(self, request, *args, **kwargs):
        room_name = self.request.session.get('room_name')
        username = self.request.session.get('username')
        room = Room.objects.filter(name=room_name).first()
        form = RoomSettings(request.POST, request.FILES, instance=room)  # replace with your actual form class

        if form.is_valid():
            form.save()
            return redirect(f'{reverse("showcase:room", kwargs={"room": room_name})}?username={username}')

        return render(request, self.template_name, {'form': form})


def getMessages(request, room):
    try:
        room_details = Room.objects.get(name=room)
    except Room.DoesNotExist:
        # Handle case where the room doesn't exist yet (e.g., return an empty response or retry logic)
        return JsonResponse({'messages': []})  # Empty message list

    messages = Message.objects.filter(room=room)

    messages_data = []
    for message in messages:
        profile_details = ProfileDetails.objects.filter(user=message.signed_in_user).first()
        if profile_details:
            user_profile_url = message.get_profile_url()
            avatar_url = profile_details.avatar.url
        else:
            user_profile_url = ('/home/' + room + '/?username=' + request.user.username)
            avatar_url = staticfiles_storage.url('css/images/a.jpg')

        message_data = {
            'user_profile_url': user_profile_url,
            'avatar_url': avatar_url,
            'user': message.user,
            'value': message.value,
            'date': message.date.strftime("%Y-%m-%d %H:%M:%S"),
            'message_number': message.message_number,
            'file': message.file.url if message.file else None,
        }

        messages_data.append(message_data)

    return JsonResponse({'messages': messages_data})


def supportroom(request):
    username = request.user.username
    room_details = SupportChat.objects.get(name=username)
    profile_details = ProfileDetails.objects.filter(
        user__username=username).first()
    return render(request, 'supportroom.html', {
        'username': username,
        'room': room_details,
        'room_details': room_details,
        'profile_details': profile_details,
    })


def index(request):
    generalmessages = Message.objects.filter(room='GeneralChatMessages').order_by('-date')
    messages = SupportMessage.objects.filter(room=request.user.username).order_by('-timestamp')
    return render(request, 'index.html', {'messages': messages})


def supportchat(request):
    return render(request, 'supportchat.html')


def privateroom(request, room):
    username = request.user.username
    room_details = Room.objects.get(name=room)
    return render(request, 'privateroom.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def supportcheckview(request):
    help = request.POST['help']
    # user = request.POST['username'] #based off def checkview
    username = request.user.username

    if SupportChat.objects.filter(name=username).exists():
        new_message = SupportMessage.objects.create(value=help,
                                                    user=username,
                                                    room=username)
        new_message.save()
        # return redirect('/supportchat/room')
        return redirect('/supportchat/room/' + username)
    else:
        new_room = SupportChat.objects.create(name=username)
        new_room.save()

        new_message = SupportMessage.objects.create(value=help,
                                                    user=username,
                                                    room=username)
        new_message.save()

        # return redirect('/supportchat/room')
        return redirect('/supportchat/room/' + username)
        print('support message sent')


def supportsend(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        username = request.POST.get('username')
        room = request.POST.get('username')
        # room_id = request.POST.get('room_id')
        # profile = request.POST.get('profile')
        # signed_in_user = request.POST.get('signed_in_user')

        print(f"message: {message}, username: {username}, room_name: {username}")
        print('this is where it is from')
        # print(f"profile: {profile}")
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # User is authenticated, use their user ID for the message user field
            new_message = SupportMessage.objects.create(
                value=message,
                user=username,
                room=username,
                # room=room_id,
                signed_in_user=request.user  # Set the signed_in_user to the authenticated user
            )
            # print(f"signed_in_user: {signed_in_user}")
            new_message.save()
        else:
            # User is not authenticated, use the provided username for the message user field
            new_message = SupportMessage.objects.create(
                value=message,
                user=username,
                room=username,
            )
            new_message.save()

        # Return a response indicating the message was sent successfully
        return HttpResponse('Message sent successfully')

    # If the request method is not POST, handle the appropriate response here
    return HttpResponse('Invalid request method. Please use POST to send a message.')


import django
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import UpdateProfile, EmailField
from .models import Idea
from .models import Vote
from .models import Choice
from .models import StaffApplication
from .models import Contact
from .models import BusinessMailingContact
from .models import PartnerApplication
from .models import PunishmentAppeal
from .models import BanAppeal
from .models import ReportIssue
from .models import NewsFeed
from .models import StaffProfile
from .models import Event
from .models import City, Vote, UpdateProfile, Idea, PartnerApplication
from .models import Support
from .models import CheckoutAddress
from .models import Item
from .models import FaviconBase
from .models import BackgroundImage
from .models import EBackgroundImage
from .models import ShowcaseBackgroundImage
from .models import ChatBackgroundImage
from .models import SupportChatBackgroundImage
from .models import BilletBackgroundImage
from .models import PatreonBackgroundImage
from .models import BusinessMessageBackgroundImage
from .models import Patreon
from .models import BlogBackgroundImage
from .models import PostBackgroundImage
from .models import PosteBackgroundImage
from .models import VoteBackgroundImage
from .models import RuleBackgroundImage
from .models import AboutBackgroundImage
from .models import FaqBackgroundImage
from .models import StaffBackgroundImage
from .models import InformationBackgroundImage
from .models import TagBackgroundImage
from .models import UserBackgroundImage
from .models import StaffRanksBackgroundImage
from .models import StaffApplyBackgroundImage
from .models import MegaBackgroundImage
from .models import EventBackgroundImage
from .models import NewsBackgroundImage
from .models import DonorBackgroundImage
from .models import ContributorBackgroundImage
from .models import ContentBackgroundImage
from .models import PartnerBackgroundImage
from .models import ShareBackgroundImage
from .models import WhyBackgroundImage
from .models import ProductBackgroundImage
from .models import SettingsModel
from .models import ImageCarousel
from .models import PostLikes
from .models import ConvertBackgroundImage
from .models import ReasonsBackgroundImage
from .models import SettingsBackgroundImage
from .models import PunishAppsBackgroundImage
from .models import BanAppealBackgroundImage
from .models import SupportBackgroundImage
from .models import OrderBackgroundImage
from .models import CheckoutBackgroundImage
from .models import SignupBackgroundImage
from .models import PerksBackgroundImage
from .models import ChangePasswordBackgroundImage
from .models import IssueBackgroundImage
from .models import BackgroundImageBase
from .models import TextBase
from .models import LogoBase
from .models import MemberHomeBackgroundImage
from .models import NavBar
from .models import NavBarHeader
from .models import DonateIcon
from .models import Donate
from .models import Titled
from .models import AdvertisementBase
from .models import ImageBase
from .models import SocialMedia
from .models import AdminRoles
from .models import AdminTasks
from .models import AdminPages
# from .models import Background2aImage
from .forms import PosteForm, EmailForm
from .forms import PostForm
from .forms import Postit
from .forms import StaffJoin
from .forms import Server_Partner
from .forms import SignUpForm
from .forms import News_Feed
from .forms import PunishAppeale
from .forms import ReportIssues
from .forms import BanAppeale
from .forms import Staffprofile
from .forms import Eventform
from .forms import ProfileDetail
from .forms import SupportForm
from .forms import SettingsForm
from .forms import BackgroundImagery
from .forms import EBackgroundImagery
from .forms import ShowcaseBackgroundImagery
from .forms import ChatBackgroundImagery
from .forms import BilletBackgroundImagery
from .forms import BlogBackgroundImagery
from .forms import PostBackgroundImagery
from .forms import RuleBackgroundImagery
from .forms import AboutBackgroundImagery
from .forms import FaqBackgroundImagery
from .forms import StaffBackgroundImagery
from .forms import InformationBackgroundImagery
from .forms import TagBackgroundImagery
from .forms import UserBackgroundImagery
from .forms import StaffRanksBackgroundImagery
from .forms import MegaBackgroundImagery
from .forms import EventBackgroundImagery
from .forms import NewsBackgroundImagery
from .forms import PaypalPaymentForm
from .forms import BaseCopyrightTextField
from .forms import ContactForme
from .forms import SignUpForm
# from .forms import OrderItems
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.db.models import Q
from django.views import generic
from django.views.generic import TemplateView, ListView

from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .forms import ProfileForm
from django.contrib.auth.models import User
from .models import Blog
from .models import Comment
from .models import UserProfile2
from django.views.generic.edit import FormMixin

import pdb
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from .forms import ContactForm
from .forms import BusinessContactForm
from .forms import BusinessMailingForm
from .forms import CommentForm
from django.shortcuts import get_object_or_404

from .models import Room, Message
from .models import SupportChat, SupportMessage
from django.http import JsonResponse
import os

from django.contrib.auth.decorators import login_required

from guest_user.mixins import RegularUserRequiredMixin

from guest_user.decorators import allow_guest_user

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from datetime import datetime
from django.utils import timezone
from .forms import CheckoutForm
from .models import (Item, OrderItem, Order, Address, Payment, Coupon, Refund,
                     UserProfile)

from django.views.generic.edit import FormView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SignupView(FormMixin, ListView):
    model = SignupBackgroundImage
    template_name = "cv-form.html"
    form_class = SignUpForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup'] = SignupBackgroundImage.objects.all()
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        return context

    def post(self, request, *args, **kwargs):
        print('signup')
        if request.method == 'POST':
            print('post')
            form = SignUpForm(request.POST)
            if form.is_valid():
                print('is_valid')
                user = form.save()
                user.refresh_from_db()
                # load the profile instance created by the signal
                user.save()
                raw_password = form.cleaned_data.get('password')

                # login user after signing up
                user = form.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                subject = "Welcome to IntelleX!"
                message = 'Hello {user.username}, thank you for becoming a member of the IntelleX Community!'
                email_from = settings.EMAIL_HOST_USER
                recipent_list = [user.email, ]
                send_mail(subject, message, email_from, recipent_list)

                # redirect user to home page
                return redirect('showcase:showcase')
                messages.info(request, "You have signed up successfully! Welcome!")
        else:
            form = SignUpForm()
        return render(request, 'cv-form.html', {'form': form})


class TotalView(ListView):
    model = BackgroundImageBase

    def _context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['TextFielde'] = TextBase.objects.filter(is_active=1).order_by("section")
        return context


class LogoView(ListView):
    model = LogoBase

    # ought to span multiple pages, not simply index

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Logo'] = LogoBase.objects.filter('page')
        return context


from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile

from .models import Advertising


class AdvertisementView(ListView):
    model = AdvertisementBase

    def display_advertisement(request, advertisement_id):
        advertising = Advertising.objects.get(id=advertising_id)
        context = {'advertising': advertising}
        return render(request, 'index.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Advertisement'] = AdvertisementBase.objects.filter(page=self.template_name, is_active=1)
        return context


"""    def handle_uploaded_image(i):
       # resize image
       imagefile  = StringIO.StringIO(i.read())
       imageImage = Image

       (width, height) = imageImage.size
       (width, height) = scale_dimensions(width, height, longest_side=240)

       resizedImage = imageImage.resize((width, height))

       imagefile = StringIO.StringIO()
       resizedImage.save(imagefile,'JPEG')"""


def set_image_position(image_id, xposition, yposition):
    # Retrieve the Image object from the database
    image = ImageBase.objects.get(id=image_id)
    print("Current coordinates: x={image.x}, y={image.y}")

    # Set the x and y positions to the desired values
    image.x = xposition
    image.y = yposition

    # Save the updated Image object back to the database
    image.save()


class ImageView(ListView):
    model = ImageBase

    def post(self, request, *args, **kwargs):
        # Get the image ID and new position values from the request
        image_id = request.POST.get('image_id')
        xposition = request.POST.get('xposition')
        yposition = request.POST.get('yposition')

        # Update the image position in the database
        set_image_position(image_id, xposition, yposition)

        # Render a response to the user
        return HttpResponse('Image position updated.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Image'] = ImageBase.objects.filter(page=self.template_name, is_active=1)
        return context


class BaseView(ListView):
    template_name = "base.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['FeaturedNavigation'] = FeaturedNavigationBar.objects.filter(is_active=1).order_by("position")
        context['Logo'] = LogoBase.objects.filter(is_active=1)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        return context


class EBaseView(ListView):
    template_name = "ebase.html"
    model = NavBar

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        context = {}
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logos'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        return context


class BlogBaseView(ListView):
    template_name = "blogbase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['FeaturedNavigation'] = FeaturedNavigationBar.objects.filter(is_active=1).order_by("position")
        context['Logo'] = LogoBase.objects.filter(is_active=1)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        return context


from .models import Preference


def detail_post_view(request, id=None):
    eachpost = get_object_or_404(Post, id=id)

    context = {'eachpost': eachpost}

    return render(request, 'showcase:likes.html', context)


@login_required
def postpreference(request, post_name, like_or_dislike):
    if request.method == "POST":
        eachpost = get_object_or_404(Blog, slug=post_name)

        if request.user in eachpost.likes.iterator():
            eachpost.likes.remove(request.user)
        if request.user in eachpost.dislikes.iterator():
            eachpost.dislikes.remove(request.user)

        if int(like_or_dislike) == 1:
            eachpost.likes.add(request.user)
        else:
            eachpost.dislikes.add(request.user)

        context = {'eachpost': eachpost,
                   'post_name': post_name}

        return render(request, 'likes.html', context)

    else:
        eachpost = get_object_or_404(Blog, slug=post_name)
        context = {'eachpost': eachpost,
                   'post_name': post_name}

        return render(request, 'showcase:likes.html', context)


# like is not connected to blog yet is used to filter

# id is used by this model but the blogpost uses slugs
from django.contrib.admin.views.decorators import staff_member_required
from django.views import View
from django.utils.decorators import method_decorator


@method_decorator(staff_member_required, name='dispatch')
class AdminRolesView(BaseView):
    template_name = "administrativeroles.html"
    model = AdminRoles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Roles'] = AdminRoles.objects.filter(is_active=1)

        return context


@method_decorator(staff_member_required, name='dispatch')
class AdminTasksView(BaseView):
    template_name = "administrativetasks.html"
    model = AdminTasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Tasks'] = AdminTasks.objects.filter(is_active=1)
        return context


@method_decorator(staff_member_required, name='dispatch')
class AdminPagesView(BaseView):
    template_name = "administrativepages.html"
    model = AdminPages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Pages'] = AdminPages.objects.filter(is_active=1)
        AdminPage = AdminPages.objects.filter(is_active=1)

        return context


@method_decorator(staff_member_required, name='dispatch')
class AdministrationView(ListView):
    template_name = "administration.html"
    model = AdminPages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Pages'] = AdminPages.objects.filter(is_active=1)
        context['Tasks'] = AdminTasks.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        return context


class DonateBaseView(ListView):
    template_name = "donatebase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        return context


class ShippingBackgroundView(FormMixin, LoginRequiredMixin, ListView):
    model = UserProfile2
    template_name = "shippingform.html"
    form_class = ShippingForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ShippingForm(user=self.request.user)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        return context

    # @login_required
    def post(self, request, *args, **kwargs):
        form = ShippingForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Shipping fields updated successfully.')
            return redirect('showcase:tradingcentral')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "shippingform.html", {'form': form})


class PrintShippingLabelView(LoginRequiredMixin, ListView):
    model = TradeShippingLabel
    template_name = "printandship.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Label'] = TradeShippingLabel.objects.filter(is_active=1, user=self.request.user)

        return context


class MemberBaseView(ListView):
    template_name = "memberbase.html"
    model = LogoBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        return context


class usersview(ListView):
    paginate_by = 10
    template_name = 'users.html'

    def get_queryset(self):
        return Idea.objects.all()


from django.db.models import Count, F


class PostList(BaseView):
    model = BlogBackgroundImage
    # backgroundqueryset = BackgroundImageBase.objects.filter('page').order_by('position')
    # queryset = Blog.objects.filter(status=1).order_by('-created_on')
    # normally can only filter once per view
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        print(124)
        context = super().get_context_data(**kwargs)
        paginate_by = int(self.request.GET.get('paginate_by', settings.DEFAULT_PAGINATE_BY))

        blog_query = Blog.objects.filter(is_active=1)
        paginator = Paginator(blog_query, paginate_by)
        page_number = self.request.GET.get('page')
        paginated_blog = paginator.get_page(page_number)

        # Annotate each blog post with the difference between the number of likes and dislikes
        PopularBlogOrder = Blog.objects.annotate(like_dislike_diff=Count(F('likes')) - Count(F('dislikes'))).order_by(
            '-like_dislike_diff', '-created_on')

        # Order the blog posts by this difference
        PopularBlogOrder = PopularBlogOrder.order_by('-like_dislike_diff')

        # Pass the ordered blog posts to the template
        context = {'PopularBlogOrder': PopularBlogOrder}

        context['BlogBackgroundImage'] = BlogBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['TextFielde'] = TextBase.objects.filter(is_active=1)
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Image'] = ImageBase.objects.filter(page=self.template_name, is_active=1).order_by("image_position")
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Social'] = SocialMedia.objects.filter(page=self.template_name, is_active=1).order_by('image_position')
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['BlogFilter'] = BlogFilter.objects.filter(is_active=1).order_by('clicks')
        context['BlogHeader'] = BlogHeader.objects.filter(is_active=1).order_by('category')
        context['blog_count'] = BlogHeader.objects.filter(is_active=1).order_by('category').count()
        context['Email'] = EmailField.objects.filter(is_active=1)
        context['form'] = EmailForm()

        context['blogpagination'] = paginated_blog

        comments = Comment.objects.filter(active=True, is_active=1).order_by('-created_on')

        context['Comments'] = comments

        for comments in context['Comments']:
            commentator = comments.commentator
            profile = ProfileDetails.objects.filter(user=commentator).first()
            if profile:
                comments.author_profile_picture_url = profile.avatar.url
                comments.author_profile_url = comments.get_profile_url()

                print('imgsrcimg')

        # Retrieve the signed-in user's profile and profile picture URL

        # Retrieve the author's profile avatar
        blog_posts = Blog.objects.filter(status=1).order_by('-created_on')

        context['BlogPosts'] = blog_posts

        for blog_post in context['BlogPosts']:
            author = blog_post.author
            profile = ProfileDetails.objects.filter(user=author).first()
            if profile:
                blog_post.author_profile_picture_url = profile.avatar.url
                blog_post.author_profile_url = blog_post.get_profile_url()

                print('imgsrcimg')

        return context

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:emaildone')
        else:
            messages.error(request, "Form submission invalid")
            print("there was an error in registering the email")
            return render(request, "blog.html", {'form': form})

    def get_blog_count():
        return Blog.objects.all().count()

    def get_queryset(self):
        return Blog.objects.filter(status=1).order_by('-created_on')


class votingview(ListView):
    model = VoteBackgroundImage
    paginate_by = 10
    template_name = 'voting.html'

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')

            return render(request, "emaildone.html", {'form': form})
            # return redirect('showcase:emaildone')  # possibly change to a finished email registration page
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "voting.html", {'form': form})
            return redirect('showcase:voting')

    def get(self, request, *args, **kwargs):
        form = EmailForm()
        self.object_list = self.get_queryset()  # Add this line
        context = self.get_context_data(**kwargs)  # Call get_context_data here
        return render(request, "voting.html", {'form': form, **context})

    def get_queryset(self):
        return VoteBackgroundImage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Vote'] = Vote.objects.all()

        newprofile = Vote.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context

    def get_queryset(self):
        return Vote.objects.all()


class CreateItemView(FormMixin, LoginRequiredMixin, ListView):
    model = Item
    paginate_by = 10
    template_name = 'create_product.html'
    form_class = ItemForm

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super(CreateItemView, self).get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Item'] = Item.objects.filter(is_active=1)

        newprofile = Item.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context

    def get(self, request, *args, **kwargs):
        form = ItemForm()
        context = self.get_context_data()
        context['form'] = form
        return render(request, 'create_product.html', context)

    def post(self, request, *args, **kwargs):
        form = ItemForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:ehome')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            form = ItemForm()
        return render(request, 'create_product.html', {'form': form})

    def profileview(request):
        instance = Item.objects.get(pk=1)
        fields = []
        for field in instance._meta.get_fields():
            fields.append({
                'name': field.name,
                'value': getattr(instance, field.name),
            })
        return render(request, 'some_template.html', {'fields': fields})


class TradeItemCreateView(ListView):
    model = TradeItem
    template_name = 'tradingcentral.html'
    success_url = '/tradingcentral/'

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['TradeItems'] = TradeItem.objects.filter(is_active=1)
        context['TradeOffers'] = TradeOffer.objects.filter(is_active=1)
        context['Friends'] = Friend.objects.filter(user=self.request.user, is_active=1)
        tradeoffering = RespondingTradeOffer.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")

        trade_offers = TradeOffer.objects.filter(is_active=1)

        slug = self.kwargs.get('slug')

        # Check if a valid slug is provided
        if slug:
            # Retrieve all feedback objects with the same slug
            trade_objects = TradeOffer.objects.filter(slug=slug)

            # Add the feedback_objects to the context
            context['TradeOffered'] = trade_objects

        return context


class TradeBackgroundView(FormMixin, LoginRequiredMixin, ListView):
    model = TradeItem
    template_name = "tradeitems.html"
    form_class = TradeItemForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['TradeItem'] = TradeItem.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        return context

    def post(self, request, *args, **kwargs):
        form = TradeItemForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:tradingcentral')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            form = TradeItemForm()
        return render(request, 'tradeitems.html', {'form': form})


class TradeOfferCreateView(CreateView):
    model = TradeOffer
    form_class = TradeProposalForm
    template_name = 'createtradeoffer.html'
    success_url = '/tradingcentral/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        form = TradeProposalForm(self.request.POST or None, user=self.request.user)
        context['form'] = form  # Add the form to the context
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['TradeOffer'] = TradeOffer.objects.filter(is_active=1)

        return context

def contact_trader(self, request, trade_item_id):
    trade_item = get_object_or_404(TradeItem, id=trade_item_id)
    current_user = request.user

    # Create a room with the current user and the trade item's user
    room = trade_item.create_room(current_user)

    # Redirect to the room view with the room name and current user
    return redirect('showcase:room', room=room.name, username=current_user.username)


class ResponseTradeOfferCreateView(CreateView):
    model = RespondingTradeOffer
    form_class = RespondingTradeOfferForm
    template_name = 'responsetradeitems.html'
    success_url = '/directedtradeoffers/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_form_instance(self):
        form = self.form_class(self.request.POST or None, user=self.request.user)
        form.fields['offered_trade_items'].queryset = TradeItem.objects.filter(user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form_instance()
            if form.is_valid():
                trade_request = form.save(commit=False)
                trade_request.user = request.user

                # Check if a RespondingTradeOffer with the same slug and user already exists
                existing_offer = RespondingTradeOffer.objects.filter(slug=trade_request.slug, user=request.user).first()
                if existing_offer:
                    # If it does, delete the existing offer
                    existing_offer.delete()

                form.save()

                # Save the RespondingTradeOffer instance first
                trade_request.save()

                # Now you can access the related TradeOffer instance
                trade_request.user2 = trade_request.wanted_trade_items.user
                trade_request.save()

                return redirect('showcase:directedtradeoffers')

        context = {'form': self.get_form_instance()}
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form_instance()  # Add the form to the context
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['TradeOffer'] = TradeOffer.objects.filter(is_active=1)

        return context


@login_required
def contact_trader(request):
    trade_item_id = request.pk
    trade_item = get_object_or_404(TradeItem, id=trade_item_id)
    current_user = request.user

    # Create a room with the current user and the trade item's user
    room = trade_item.create_room(current_user)

    # Redirect to the room view with the room name and current user
    return redirect('showcase:room', room=room.name, username=current_user.username)


@method_decorator(login_required, name='dispatch')
class FriendRequestsView(View):
    def get(self, request, *args, **kwargs):
        # Get all pending friend requests for the current user
        pending_requests = FriendRequest.objects.filter(receiver=request.user, status=FriendRequest.PENDING)
        outgoing_requests = FriendRequest.objects.filter(sender=request.user, status=FriendRequest.PENDING)

        context = {}
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        profiles = []
        for newprofile in FriendRequest.objects.filter(Q(sender=request.user) | Q(receiver=request.user)):
            user = newprofile.sender if newprofile.sender != request.user else newprofile.receiver
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url(request.user)
                profiles.append(newprofile)

        context['Profiles'] = profiles

        if is_ajax(request):
            context.update({'pending_requests': pending_requests, 'outgoing_requests': outgoing_requests})
            return render(request, 'my_friend_request.html', context)

        context.update({'pending_requests': pending_requests, 'outgoing_requests': outgoing_requests})
        return render(request, 'my_friend_requests.html', context)


from django.contrib import messages


@login_required
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    print('friend request acceptance')
    if request.user != friend_request.receiver:
        raise PermissionDenied
    friend_request.status = FriendRequest.ACCEPTED
    friend_request.save()
    messages.success(request, 'You have accepted the friend request.')
    return redirect('showcase:my_friend_requests')


@login_required
def decline_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    if request.user != friend_request.receiver:
        raise PermissionDenied
    friend_request.status = FriendRequest.DECLINED
    friend_request.save()
    messages.success(request, 'You have declined the friend request.')
    return redirect('showcase:my_friend_requests')


class FriendlyView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        friends = user.get_friends()
        print(friends)
        context = {'friends': friends, 'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
                   'DropDown': NavBar.objects.filter(is_active=1).order_by('position')}
        current_user = request.user

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return render(request, 'my_friends.html', context)


@method_decorator(login_required, name='dispatch')
class SendFriendRequestView(View):
    def post(self, request):
        form = FriendRequestForm(request.POST)
        if form.is_valid():
            friend_request = form.save(commit=False)
            friend_request.sender = request.user

            # Check if a FriendRequest with the same sender and receiver already exists
            if not FriendRequest.objects.filter(sender=friend_request.sender,
                                                receiver=friend_request.receiver).exists():
                friend_request.save()
                return HttpResponseRedirect('/my_friend_requests')
            else:
                messages.error(request,
                               "You already sent a friend request to that user or you are already friends with them!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            # Handle the case where the form is not valid
            messages.error(request, "Please send a friend request to the trader to continue.")
            return render(request, 'send_friend_request.html', {'form': form})

    def get(self, request):
        form = FriendRequestForm()
        context = {}
        context['form'] = form
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        return render(request, 'send_friend_request.html', context)


from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def contact_trader(request, trade_offer_id):
    trade_offer = TradeOffer.objects.get(id=trade_offer_id)
    current_user = request.user

    # Check if there's an accepted friend request between the current user and the trade offer creator
    if not FriendRequest.objects.filter(
            Q(sender=trade_offer.user, receiver=current_user, status=FriendRequest.ACCEPTED) |
            Q(sender=current_user, receiver=trade_offer.user, status=FriendRequest.ACCEPTED)
    ).exists():
        # If not, create a new friend request with status pending
        FriendRequest.objects.create(sender=current_user, receiver=trade_offer.user, status=FriendRequest.PENDING)
    else:
        # If there's an accepted friend request, check if a private room already exists between the two users
        room = Room.objects.filter(signed_in_user__in=[current_user, trade_offer.user], public=False).first()
        if not room:
            # If not, create a new private room
            room = Room.objects.create(name=f'Private room: {current_user.username} and {trade_offer.user.username}',
                                       signed_in_user=current_user, public=False)

        # Redirect to the room page
        return redirect(room.get_absolute_url())


class partnerview(ListView):
    paginate_by = 10
    template_name = 'partners.html'

    def get_queryset(self):
        return PartnerApplication.objects.all()


class newsfeedview(ListView):
    paginate_by = 10
    template_name = 'newsfeed.html'

    def get_queryset(self):
        return NewsFeed.objects.all()


class Issueview(ListView):
    paginate_by = 10
    template_name = 'issues.html'

    def get_queryset(self):
        return ReportIssue.objects.all()


class staffview(ListView):
    paginate_by = 10
    template_name = 'staff.html'

    def get_queryset(self):
        return StaffProfile.objects.all()


class eventview(ListView):
    paginate_by = 10
    template_name = 'events.html'

    def get_queryset(self):
        return Event.objects.all()


"""class SupportRoomView(TemplateView):
    model = SupportMessage
    template_name = 'supportroom.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.kwargs['room']
        username = self.request.GET.get('username')
        room_details = Room.objects.get(name=room)
        profile_details = ProfileDetails.objects.filter(user__username=username).first()
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')

        context['username'] = username
        context['room'] = room
        context['room_details'] = room_details
        context['profile_details'] = profile_details

        # Retrieve the author's profile avatar
        messages = Message.objects.all().order_by('-date')

        context['Messaging'] = messages

        for messages in context['Messaging']:
            profile = ProfileDetails.objects.filter(user=messages.signed_in_user).first()
            if profile:
                messages.user_profile_picture_url = profile.avatar.url
                messages.user_profile_url = messages.get_profile_url()

        return context"""


class SupportRoomView(TemplateView):
    model = SupportMessage
    template_name = 'supportroom.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        signed_in_user = self.kwargs['signed_in_user']
        # room_name = self.kwargs['room_name']
        context['username'] = signed_in_user  # Set 'username' to the extracted 'signed_in_user'

        # room = self.kwargs['room']
        # room_details = SupportChat.objects.get(name=signed_in_user)  # Use 'signed_in_user' here
        profile_details = ProfileDetails.objects.filter(user__username=signed_in_user).first()
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['room'] = signed_in_user
        context['profile_details'] = profile_details

        # Retrieve the author's profile avatar
        # Retrieve the messages
        messages = SupportMessage.objects.all().order_by('-date')

        context['Messanger'] = messages

        # Create a list to store formatted message data
        messages_data = []

        for messages in context['Messanger']:
            profile = ProfileDetails.objects.filter(user=messages.signed_in_user).first()

            # Create a dictionary to store message data including profile information
            message_data = {
                'user_profile_picture_url': profile.avatar.url if profile else '',
                'user_profile_url': messages.get_profile_url(),
                'user': messages.signed_in_user,
                'value': messages.value,
                'date': messages.date,
            }

            messages_data.append(message_data)

        # Assign the list of formatted message data to the context
        context['Messanger'] = messages_data

        return context


def supportroom(request, signed_in_user):
    return render(request, 'supportroom.html', {
        'username': username,
        'supportroom': supportroom,
        'signed_in_user': signed_in_user,
        'room_details': room_details,
        'profile_details': profile_details,
        'Logo': Logo,
        'Header': Header,
        'Dropdown': DropDown,
    })


class SupportCombinedView(SupportRoomView, ListView):
    paginate_by = 10
    template_name = 'supportroom.html'

    def get_queryset(self):
        return SupportMessage.objects.all()


class supportview(ListView):
    paginate_by = 10
    template_name = 'supportissues.html'

    def get_queryset(self):
        return Support.objects.all()


class SupportLineView(TemplateView):
    model = SupportLine
    template_name = 'supportline.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.kwargs['room']
        username = self.request.GET.get('username')
        room_details = SupportInterface.objects.get(name=room)
        profile_details = ProfileDetails.objects.filter(user__username=username).first()
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['username'] = username
        context['room'] = room
        context['room_details'] = room_details
        context['profile_details'] = profile_details

        # Retrieve the author's profile avatar
        messages = SupportLine.objects.all().order_by('-date')

        context['Messaging'] = messages

        for messages in context['Messaging']:
            profile = ProfileDetails.objects.filter(user=messages.signed_in_user).first()
            if profile:
                messages.user_profile_picture_url = profile.avatar.url
                messages.user_profile_url = messages.get_profile_url()

        return context


def supportline(request, room):
    username = request.user.username
    room_details = SupportInterface.objects.get(name=username)
    profile_details = ProfileDetails.objects.filter(
        user__username=username).first()
    return render(request, 'supportline.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
        'profile_details': profile_details,
    })


def supportlinecheckview(request):
    room = request.POST['room_name']

    if SupportInterface.objects.filter(name=room).exists():
        # return redirect('/supportchat/room')
        return redirect('/supportinterface/room/' + room)
    else:
        new_room = SupportInterface.objects.create(name=room)
        signed_in_user = request.user
        print('the room owner is ' + str(signed_in_user))
        new_room.save()
        # return redirect('/supportchat/room')
        return redirect('/supportinterface/room/' + room)


from django.shortcuts import get_object_or_404


def supportlinesend(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        username = request.POST.get('username')
        room_id = request.POST.get('room_id')

        print(f"message: {message}, username: {username}, room_id: {room_id}")

        # Check if the user is authenticated and has permission to send a message
        if request.user.is_authenticated and request.user.is_staff:
            # User is authenticated, use their user ID for the message user field
            user = request.user  # Use the authenticated user

        # Create a new SupportLine message with the correct room and user
        new_message = SupportLine.objects.create(
            value=message,
            user=user,  # Assign the user to the message
            room=room_id,
            signed_in_user=request.user if request.user.is_authenticated else None
        )

        # Return a response indicating the message was sent successfully
        return HttpResponse('Message sent successfully')

    # If the request method is not POST or the user is not authorized, handle the appropriate response here
    return HttpResponse('Invalid request or authorization.')


def supportlinegetMessages(request, room, **kwargs):
    room_details = SupportInterface.objects.get(name=room)
    messages = SupportLine.objects.filter(room=room)
    # Check if the user is authenticated
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden("You do not have permission to access this chat room")

    chat_room = get_object_or_404(SupportInterface, name=room)

    # Check if the requesting user is the creator of the room or an administrator
    if request.user.is_staff:
        # Retrieve messages for the specified room
        messages = SupportLine.objects.filter(room=chat_room)
        messages_data = []

        for message in messages:
            profile_details = ProfileDetails.objects.filter(user=message.signed_in_user).first()
            if profile_details:
                user_profile_url = message.get_profile_url()
                avatar_url = profile_details.avatar.url
            else:
                user_profile_url = f'/supportline/{message.signed_in_user}'
                avatar_url = staticfiles_storage.url('css/images/a.jpg')

            messages_data.append({
                'user_profile_url': user_profile_url,
                'avatar_url': avatar_url,
                'user': message.signed_in_user.username,
                'value': message.value,
                'date': message.date.strftime("%Y-%m-%d %H:%M:%S"),
                'message_number': message.message_number,
            })

        return JsonResponse({'messages': messages_data})
    else:
        return HttpResponseForbidden("You do not have permission to access this chat room")


class MemberHomeBackgroundView(ListView):
    model = MemberHomeBackgroundImage
    template_name = "memberhome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['PatreonBackgroundImage'] = PatreonBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['MemberHomeBackgroundImage'] = MemberHomeBackgroundImage.objects.all()
        return context


class BusinessMessageBackgroundView(ListView):
    model = BusinessMessageBackgroundImage
    template_name = "businessemail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['PatreonBackgroundImage'] = PatreonBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BusinessMessageBackgroundImage'] = BusinessMessageBackgroundImage.objects.all()
        return context


class PatreonBackgroundView(ListView):
    model = Patreon
    template_name = "patreon.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['PatreonBackgroundImage'] = PatreonBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        # context['Patreon'] = Patreon.objects.all()
        return context


"""class BlogComment(generic.DetailView):
    model = Blog
    paginate_by = 10
    template_name = 'blog_comment.html'

    def post(self, request, slug, *args, **kwargs):
        most_recent = Blog.objects.order_by('-created_on')[:3]

        post = get_object_or_404(Blog, slug=slug)
        category_count = post.likes

        # if request.user.is_authenticated:
        #    BlogLikeView.objects.get_or_create(user=request.user, post=post)

        form = CommentForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                form.instance.user = request.user
                form.instance.post = post
                form.save()
                return redirect(reverse("blog_comment", kwargs={
                    'id': post.pk
                }))
        context = {
            'form': form,
            'post': post,
            'most_recent': most_recent,
            'category_count': category_count,
            'form': form
        }
        return render(request, 'blog_comment.html', context)"""

# def BlogPostLike(request, slug):
#    post = get_object_or_404(Blog, id=request.POST.get('blog_id'))
#    if post.likes.filter(id=request.user.id).exists():
#        post.likes.remove(request.user)
#    else:
#        post.likes.add(request.user)

#    return HttpResponseRedirect(reverse('showcase:post_detail', args=[str(slug)]))


# class BackgroundView(ListView):
#  paginate_by = 10
#  template_name = 'index.html'

#  def get_queryset(self):
#    return BackgroundImage.objects.all()

from django.views.generic import ListView, CreateView


# class TextFieldView(ListView):
#    model = TextField
#    template_name = "index.html"


class FaviconBaseView(ListView):
    model = FaviconBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Favicons'] = FaviconBase.objects.filter('faviconpage')
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        return context


class BackgroundBaseView(ListView):
    model = BackgroundImageBase

    # ought to span multiple pages, not simply index

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BackgroundImages'] = BackgroundImageBase.objects.filter('page').order_by('position')
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        return context

    # def backgrounds(request, showcase, index, blog):
    #    page = get_object_or_404(BackgroundImageBase,
    #                             showcase=showcase,
    #                             index=index,
    #                             blog=blog)

    # context = {
    #    'page': page,
    # }

    # if index == 'index':
    #    template = 'index.html'
    #    print(index)
    # elif index == 'showcase':
    #    template = 'showcase.html'
    #    print(index)
    # else render the one you're already rendering
    # else:
    #    template = 'blog.html'
    #    print(index)

    # return render(request, template, context)


class TextBaseView(ListView):
    model = TextBase

    # ought to span multiple pages, not simply index

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(is_active=1).order_by("section")
        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})
        # texts = TextBase.objects.all()

        # if texts.exists():
        #    return JsonResponse({})
        # else:
        #    return context

        # def backgrounds(request, showcase, index, blog):
        #    page = get_object_or_404(BackgroundImageBase,
        #                             showcase=showcase,
        #                             index=index,
        #                             blog=blog)

        # context = {
        #    'page': page,
        # }

        # if index == 'index':
        #    template = 'index.html'
        #    print(index)
        # elif index == 'showcase':
        #    template = 'showcase.html'
        #    print(index)
        # else render the one you're already rendering
        # else:
        #    template = 'blog.html'
        #    print(index)

        return render(context)


class ImageCarouselView(BaseView):
    model = ImageCarousel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Carousel'] = ImageCarousel.objects.filter(is_active=1).order_by('position')
        return context


def index(request):
    general_messages = Message.objects.filter(room="General").order_by('-date')
    context = {'GeneralMessanger': general_messages}
    return render(request, 'index.html', context)


from django.http import HttpResponse
from .models import Message



@csrf_exempt  # Add this decorator to allow POST requests without CSRF token for testing purposes
def send(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        username = request.POST.get('username')
        room_id = request.POST.get('room_id')
        page_name = request.POST.get('page_name')

        if page_name == 'index.html':
            room_id = 'General'

        print(f"message: {message}, username: {username}, room_id: {room_id}, page_name: {page_name}")
        print('This is a community-sent message')

        if request.user.is_authenticated:
            new_message = Message.objects.create(
                value=message,
                user=username,
                room=room_id,
                signed_in_user=request.user
            )
        else:
            new_message = Message.objects.create(
                value=message,
                user=username,
                room=room_id
            )
            new_message.save()
        return JsonResponse({'message': 'Message sent successfully'})

    # Handle invalid request methods
    return HttpResponse('Invalid request method. Please use POST to send a message.')


class BackgroundView(FormMixin, BaseView):
    model = BackgroundImage
    form_class = EmailForm
    template_name = "index.html"
    section = TextBase.section

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')

            return render(request, "emaildone.html", {'form': form})
            # return redirect('showcase:emaildone')  # possibly change to a finished email registration page
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "index.html", {'form': form})
            return redirect('showcase:index')

    @login_required
    def send(request):
        if request.method == 'POST':
            message = request.POST.get('message')
            username = request.POST.get('username')
            room_name = request.POST.get('room_name')
            message_type = request.POST.get('message_type')

            if not message:
                return HttpResponse('Message content is missing', status=400)

            if message_type == 'general':
                room_name = "General"  # Override room_name for general messages
                new_message = Message.objects.create(
                    room=room_name,
                    signed_in_user=request.user,
                    value=message,
                    user=request.user.username
                )
                return HttpResponse('Message sent successfully')
            else:
                # Handle other message types, if any
                return HttpResponse('Unsupported message type', status=400)

        return HttpResponse('Invalid request method. Please use POST to send a message.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        signed_in_user = self.request.user
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['messages'] = SupportMessage.objects.filter(room=self.request.user.username).order_by('-date')
        context['friendmessages'] = Message.objects.filter(room=self.request.user.username).order_by('-date')
        context['Carousel'] = ImageCarousel.objects.filter(is_active=1, carouselpage=self.template_name).order_by(
            "carouselposition")
        context['Advertisement'] = AdvertisementBase.objects.filter(page=self.template_name, is_active=1).order_by(
            "advertisement_position")
        context['Image'] = ImageBase.objects.filter(page=self.template_name, is_active=1).order_by("image_position")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['FeaturedGame'] = Game.objects.filter(is_active=1, filter='F')
        context['Social'] = SocialMedia.objects.filter(page=self.template_name, is_active=1)
        context['Feed'] = Feedback.objects.filter(is_active=1, feedbackpage=self.template_name).order_by("slug")
        context['Email'] = EmailField.objects.filter(is_active=1)
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['About'] = Event.objects.filter(page=self.template_name, is_active=1)
        context['Feedback'] = Feedback.objects.filter(showcase=1, is_active=1)
        context['Events'] = Event.objects.filter(page=self.template_name, is_active=1)
        context['username'] = signed_in_user  # Set 'username' to the extracted 'signed_in_user'
        context['room'] = signed_in_user
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        print(FaviconBase.objects.all())
        print(213324)
        # Retrieve the signed-in user's profile and profile picture URL

        # Retrieve the items
        product = Item.objects.filter(is_active=1)

        context['Products'] = product

        for product in context['Products']:
            image = product.image
            item = Item.objects.filter(slug=product.slug).first()
            if product:
                product.title = item.title
                product.price = item.price
                product.discount_price = item.discount_price
                product.image_url = item.image.url
                product.label = item.label
                product.hyperlink = item.get_profile_url()
                product.description = item.description

        events = Event.objects.filter(is_active=1)
        context['NewEvents'] = events

        for events in context['NewEvents']:
            image = events.image
            eventful = Event.objects.filter(date_and_time=events.date_and_time).first()
            if events:
                events.name = eventful.name
                events.image_url = eventful.image.url
                events.hyperlink = eventful.get_profile_url()
                events.description = eventful.description

        newprofile = NewsFeed.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['News'] = newprofile

        for newprofile in context['News']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        feed = Feedback.objects.filter(is_active=1).order_by('-timestamp')

        if self.request.user.is_authenticated:
            userprofile = ProfileDetails.objects.filter(is_active=1, user=self.request.user)
        else:
            userprofile = None

        if userprofile:
            context['Profiles'] = userprofile
        else:
            context['Profiles'] = None

        if context['Profiles'] == None:
            # Create a new object with the necessary attributes
            userprofile = type('', (), {})()
            userprofile.newprofile_profile_picture_url = 'static/css/images/a.jpg'
            userprofile.newprofile_profile_url = None
        else:
            for userprofile in context['Profiles']:
                user = userprofile.user
                profile = ProfileDetails.objects.filter(user=user).first()
                if profile:
                    userprofile.newprofile_profile_picture_url = profile.avatar.url
                    userprofile.newprofile_profile_url = userprofile.get_profile_url()

        feed = Feedback.objects.filter(is_active=1).order_by('-timestamp')

        context['FeedBacking'] = feed

        for feed in context['FeedBacking']:
            user = feed.username
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                feed.user_profile_picture_url = profile.avatar.url
                feed.user_profile_url = feed.get_profile_url2()
                feed.feedback_profile_url = feed.get_profile_url()
                print(user)

        # Retrieve the author's profile avatar
        # Retrieve the messages

        # Messages
        messages = SupportMessage.objects.all().order_by('-date')
        context['Messanger'] = messages
        messages_data = []

        for message in context['Messanger']:
            profile_details = ProfileDetails.objects.filter(user=message.signed_in_user).first()
            message_data = {
                'user_profile_picture_url': profile_details.avatar.url if profile_details else '',
                'user_profile_url': message.get_profile_url(),
                'user': message.signed_in_user,
                'value': message.value,
                'date': message.date,
            }
            messages_data.append(message_data)

        context['Messanger'] = messages_data

        # General Messages
        general_messages = Message.objects.filter(room="General").order_by('date')
        context['GeneralMessanger'] = general_messages
        general_messages_data = []

        for general_message in general_messages:
            profile_details = ProfileDetails.objects.filter(user=general_message.signed_in_user).first()
            general_message_data = {
                'user_profile_picture_url': profile_details.avatar.url if profile_details else '',
                'user_profile_url': general_message.get_profile_url(),
                'user': general_message.signed_in_user,
                'value': general_message.value,
                'date': general_message.date,
            }
            general_messages_data.append(general_message_data)

        context['GeneralMessanger'] = general_messages_data

        return context
"""
@login_required
def get_general_messages(request, room_name):
    general_messages = Message.objects.filter(room=room_name).order_by('date')

    messages_data = []
    for message in general_messages:
        profile = ProfileDetails.objects.filter(user=message.signed_in_user).first()
        message_data = {
            'user_profile_picture_url': profile.avatar.url if profile else '',
            'user_profile_url': message.get_profile_url(),
            'user': message.signed_in_user.username,
            'value': message.value,
            'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),
        }
        messages_data.append(message_data)

    return JsonResponse({'messages': messages_data})"""

def indexsupportroom(request, signed_in_user):
    return render(request, 'index.html', {
        'username': username,
        'supportroom': supportroom,
        'signed_in_user': signed_in_user,
        'room_details': room_details,
        'profile_details': profile_details,
        'Logo': Logo,
        'Header': Header,
        'Dropdown': DropDown,
    })



def dynamic_css(request):
    background_objects = BackgroundImageBase.objects.filter(page='index').order_by("position")

    context = {
        'background_objects': background_objects,
    }

    return render(request, 'dynamic_css.css', context, content_type='text/css')


class CreatePostView(CreateView):
    model = BackgroundImage
    form_class = BackgroundImagery
    template_name = "backgroundimagechange.html"
    success_url = reverse_lazy("index")


class TermsAndConditionsView(BaseView):
    model = BackgroundImage
    form_class = EmailForm
    template_name = "termsandconditions.html"
    section = TextBase.section


class PolicyView(BaseView):
    model = BackgroundImage
    form_class = EmailForm
    template_name = "policy.html"
    section = TextBase.section


import urllib.request as url_request


def get_items_by_category(category):
    if category == 'all':
        items = Item.objects.all()
    elif category == 'gold':
        items = Item.objects.filter(category='G')
    elif category == 'platinum':
        items = Item.objects.filter(category='P')
    elif category == 'emerald':
        items = Item.objects.filter(category='E')
    elif category == 'diamond':
        items = Item.objects.filter(category='D')
    else:
        items = Item.objects.all()
    return items


from django.contrib.auth.models import AnonymousUser


class EBackgroundView(BaseView, FormView):
    model = EBackgroundImage
    template_name = "ehome.html"
    form_class = EmailForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_user = self.request.user
        total_items = Item.objects.filter(is_active=1).count()

        # Get the paginate_by value from the form data or settings
        paginate_by = int(self.request.GET.get('paginate_by', settings.DEFAULT_PAGINATE_BY))

        items_query = Item.objects.filter(is_active=1).order_by('price')
        paginator = Paginator(items_query, paginate_by)
        page_number = self.request.GET.get('page')
        paginated_items = paginator.get_page(page_number)

        # context['items'] = paginated_items

        # context['items'] = Item.objects.filter(is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Image'] = ImageBase.objects.filter(is_active=1, page=self.template_name)
        context['Social'] = SocialMedia.objects.filter(page=self.template_name, is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(page=self.template_name,
                                                                                    is_active=1)
        context['Email'] = EmailField.objects.filter(is_active=1)
        context['store_view_form'] = StoreViewTypeForm()
        context['form'] = EmailForm()

        if isinstance(current_user, AnonymousUser):
            try:
                user_store_view_type = StoreViewType.objects.filter(is_active=1).first()
                context['store_view_type_str'] = str(user_store_view_type)
                context['streamfilter_string'] = f'streamfilter set by {self.request.user.username}'
                print('store view exists')
                print(str(user_store_view_type))
            except StoreViewType.DoesNotExist:
                user_store_view_type = None
                print('store view does not exist')
        else:
            try:
                user_store_view_type = StoreViewType.objects.get(user=current_user, is_active=1)
                context['store_view_type_str'] = str(user_store_view_type)
                context['streamfilter_string'] = f'streamfilter set by {self.request.user.username}'
                print('store view exists')
                print(str(user_store_view_type))
            except StoreViewType.DoesNotExist:
                user_store_view_type = None
                print('store view does not exist')

        context['item_filters'] = ItemFilter.objects.filter(is_active=1)
        item_filters = ItemFilter.objects.filter(is_active=1)
        for item_filter in item_filters:
            print(str(item_filter))
        print(context)
        print('The item filters are:')
        items_query = Item.objects.filter(is_active=1)
        paginator = Paginator(items_query, paginate_by)
        page_number = self.request.GET.get('page')
        paginated_items = paginator.get_page(page_number)

        context['items'] = paginated_items

        category = self.request.GET.get('category', 'all')
        categoryitems = self.get_items_by_category(category)
        context['categorizeditems'] = categoryitems
        return context

    def get_items_by_category(self, category):
        if category == 'all':
            items = Item.objects.all()
        elif category == 'gold':
            items = Item.objects.filter(category='G')
        elif category == 'platinum':
            items = Item.objects.filter(category='P')
        elif category == 'emerald':
            items = Item.objects.filter(category='E')
        elif category == 'diamond':
            items = Item.objects.filter(category='D')
        else:
            items = Item.objects.all()
        return items

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'EmailForm submitted successfully.')
            try:
                email = EmailField.objects.get(user=request.user)
                profile = ProfileDetails.objects.get(user=request.user)
                profile.email = email.email
                profile.save()
            except ProfileDetails.DoesNotExist:
                messages.error(request, 'Profile details not found.')
            except EmailField.DoesNotExist:
                print("EmailField does not exist.")
            except Exception as e:
                messages.error(request, f'An error occurred: {e}')
            try:
                email = EmailField.objects.get(user=request.user)
                user = request.user
                user.email = email.email
                user.save()
            except Exception as e:
                messages.error(request, f'An error occurred: {e}')

        else:
            messages.error(request, "EmailForm submission invalid")
            print("there was an error in registering the email")

        return render(request, 'ehome.html', {'form': form})


class StoreView(BaseView, FormView, ListView):
    model = StoreViewType
    template_name = "storeviewtypesnippet.html"
    form_class = StoreViewTypeForm

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()  # Add this line
        context = self.get_context_data()
        eform = StoreViewTypeForm(request=request)
        return render(request, 'storeviewtypesnippet.html', {'eform': eform, **context})

    def get_context_data(self, **kwargs):
        context = {}
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Image'] = ImageBase.objects.filter(is_active=1, page=self.template_name)
        context['Social'] = SocialMedia.objects.filter(page=self.template_name, is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(page=self.template_name,
                                                                                    is_active=1)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        return context

    def post(self, request, *args, **kwargs):
        eform = StoreViewTypeForm(request.POST, request=request)

        if eform.is_valid():
            post = eform.save(commit=False)
            post.save()
            return redirect('showcase:ehome')
        else:
            print('the errors with the storeviewtype form are ' + str(eform.errors))
        return render(request, 'storeviewtypesnippet.html', {'eform': eform})


class ECreatePostView(CreateView):
    model = EBackgroundImage
    form_class = EBackgroundImagery
    template_name = "ebackgroundimagechange.html"
    success_url = reverse_lazy("ehome")


class ShowcaseBackgroundView(BaseView):
    model = ShowcaseBackgroundImage
    template_name = "showcase.html"
    queryset = ShowcaseBackgroundImage.objects.all()  # Add this line

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')

            return render(request, "emaildone.html", {'form': form})
            # return redirect('showcase:emaildone')  # possibly change to a finished email registration page
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "showcase.html", {'form': form})
            return redirect('showcase:showcase')

    def get(self, request, *args, **kwargs):
        form = EmailForm()
        self.object_list = self.get_queryset()  # Add this line
        context = self.get_context_data(**kwargs)  # Call get_context_data here
        return render(request, "showcase.html", {'form': form, **context})

    def get_queryset(self):
        return ShowcaseBackgroundImage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ShowcaseBackgroundImage'] = ShowcaseBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['UpdateProfile'] = UpdateProfile.objects.all()

        newprofile = UpdateProfile.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class ShowcaseCreatePostView(CreateView):
    model = ShowcaseBackgroundImage
    form_class = ShowcaseBackgroundImagery
    template_name = "showcasebackgroundimagechange.html"
    success_url = reverse_lazy("showcase")


def forbidden_access(request):
    return render(request, 'forbiddenaccess.html')


class SupportLineBackgroundView(BaseView):
    model = SupportInterface
    template_name = "supportinterface.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        return context


class ChatCreatePostView(CreateView):
    model = ChatBackgroundImage
    form_class = ChatBackgroundImagery
    template_name = "chatbackgroundimagechange.html"
    success_url = reverse_lazy("home")


class WhyBackgroundView(BaseView):
    model = WhyBackgroundImage
    template_name = "whydonate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        return context


class MemeHostView(BaseView):
    model = Meme
    template_name = "meme_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ShowcaseBackgroundImage'] = ShowcaseBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['UpdateProfile'] = UpdateProfile.objects.all()

        newprofile = Meme.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class MemeView(FormMixin, ListView):
    model = Meme
    template_name = "create_meme.html"
    form_class = MemeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Profile'] = UpdateProfile.objects.all()
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()

        newprofile = UpdateProfile.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = MemeForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                form.instance.user = request.user
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:meme_list')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "create_meme.html", {'form': form})
        else:
            form = MemeForm()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "create_meme.html", {'form': form})


class BlogBackgroundView(ListView):
    model = BlogBackgroundImage
    template_name = "blog.html"

    queryset = Blog.objects.filter(status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['BlogBackgroundImage'] = BlogBackgroundImage.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        return context


class BlogCreatePostView(CreateView):
    model = BlogBackgroundImage
    form_class = BlogBackgroundImagery
    template_name = "blogbackgroundimagechange.html"
    success_url = reverse_lazy("blog")


# @login_required
# @RegularUserRequiredMixin
class PostBackgroundView(FormMixin, LoginRequiredMixin, ListView):
    model = UpdateProfile
    template_name = "post_edit.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        return context

    # @login_required
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:showcase')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "post_edit.html", {'form': form})


class PostCreatePostView(CreateView):
    model = PostBackgroundImage
    form_class = PostBackgroundImagery
    template_name = "postbackgroundimagechange.html"
    success_url = reverse_lazy("post_edit")


class BilletBackgroundView(BaseView):
    model = BilletBackgroundImage
    template_name = "billets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BilletBackgroundImage'] = BilletBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context


class BilletCreatePostView(CreateView):
    model = BilletBackgroundImage
    form_class = BilletBackgroundImagery
    template_name = "billetbackgroundimagechange.html"
    success_url = reverse_lazy("billets")


class RuleCreatePostView(CreateView):
    model = RuleBackgroundImage
    form_class = RuleBackgroundImagery
    template_name = "rulebackgroundimagechange.html"
    success_url = reverse_lazy("rules")


class AboutBackgroundView(BaseView):
    model = AboutBackgroundImage
    template_name = "about.html"

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')

            return render(request, "emaildone.html", {'form': form})
            # return redirect('showcase:emaildone')  # possibly change to a finished email registration page
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "about.html", {'form': form})
            return redirect('showcase:newsfeed')

    def get(self, request, *args, **kwargs):
        form = EmailForm()
        self.object_list = self.get_queryset()  # Add this line
        context = self.get_context_data(**kwargs)  # Call get_context_data here
        return render(request, "about.html", {'form': form, **context})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Image'] = ImageBase.objects.filter(is_active=1, page=self.template_name)
        context['Staff'] = StaffProfile.objects.filter(is_active=1).prefetch_related('socialmedia_set')

        return context


class AboutCreatePostView(CreateView):
    model = AboutBackgroundImage
    form_class = AboutBackgroundImagery
    template_name = "aboutbackgroundimagechange.html"
    success_url = reverse_lazy("about")


class FaqBackgroundView(BaseView):
    model = FaqBackgroundImage
    template_name = "faq.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['FaqBackgroundImage'] = FaqBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Faq'] = FrequentlyAskedQuestions.objects.all().order_by("position")
        return context


class FaqCreatePostView(CreateView):
    model = FaqBackgroundImage
    form_class = FaqBackgroundImagery
    template_name = "faqbackgroundimagechange.html"
    success_url = reverse_lazy("faq")


class StaffBackgroundView(BaseView):
    model = BackgroundImage
    template_name = "staff.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context


class StaffCreatePostView(CreateView):
    model = StaffBackgroundImage
    form_class = StaffBackgroundImagery
    template_name = "staffbackgroundimagechange.html"
    success_url = reverse_lazy("staff")


class InformationBackgroundView(BaseView):
    InformationBackgroundImage
    template_name = "information.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context


class InformationCreatePostView(CreateView):
    model = InformationBackgroundImage
    form_class = InformationBackgroundImagery
    template_name = "Informationbackgroundimagechange.html"
    success_url = reverse_lazy("Information")


class TagBackgroundView(BaseView):
    model = TagBackgroundImage
    template_name = "tag.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context


class TagCreatePostView(CreateView):
    model = TagBackgroundImage
    form_class = TagBackgroundImagery
    template_name = "tagbackgroundimagechange.html"
    success_url = reverse_lazy("tag")


class UserBackgroundView(BaseView):
    model = UserBackgroundImage
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['UserBackgroundImage'] = UserBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context


class UserCreatePostView(CreateView):
    model = UserBackgroundImage
    form_class = UserBackgroundImagery
    template_name = "userbackgroundimagechange.html"
    success_url = reverse_lazy("users")


class StaffRanksBackgroundView(BaseView):
    model = StaffRanksBackgroundImage
    template_name = "staffranks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['StaffRanksBackgroundImage'] = StaffRanksBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context


class StaffRanksCreatePostView(CreateView):
    model = StaffRanksBackgroundImage
    form_class = StaffRanksBackgroundImagery
    template_name = "staffranksbackgroundimagechange.html"
    success_url = reverse_lazy("staffranks")


class MegaBackgroundView(BaseView):
    model = MegaBackgroundImage
    template_name = "megacoins.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MegaCoinsBackgroundImage'] = MegaBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context


class MegaCreatePostView(CreateView):
    model = MegaBackgroundImage
    form_class = MegaBackgroundImagery
    template_name = "megacoinsbackgroundimagechange.html"
    success_url = reverse_lazy("megacoins")


class EventBackgroundView(BaseView):
    model = EventBackgroundImage
    template_name = "events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['EventBackgroundImage'] = EventBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Events'] = Event.objects.all()

        newprofile = Event.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class EventCreatePostView(CreateView):
    model = EventBackgroundImage
    form_class = EventBackgroundImagery
    template_name = "eventbackgroundimagechange.html"
    success_url = reverse_lazy("event")


class NewsBackgroundView(ListView):
    model = NewsBackgroundImage
    form_class = EmailForm
    template_name = "newsfeed.html"
    queryset = NewsBackgroundImage.objects.all()  # Add this line

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')

            return render(request, "emaildone.html", {'form': form})
            # return redirect('showcase:emaildone')  # possibly change to a finished email registration page
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "newsfeed.html", {'form': form})
            return redirect('showcase:newsfeed')

    def get(self, request, *args, **kwargs):
        form = EmailForm()
        self.object_list = self.get_queryset()  # Add this line
        context = self.get_context_data(**kwargs)  # Call get_context_data here
        return render(request, "newsfeed.html", {'form': form, **context})

    def get_queryset(self):
        return NewsBackgroundImage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['NewsBackgroundImage'] = NewsBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['News'] = NewsFeed.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Image'] = ImageBase.objects.filter(page=self.template_name, is_active=1)
        context['Email'] = EmailField.objects.filter(is_active=1)

        newprofile = NewsFeed.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class NewsCreatePostView(CreateView):
    model = NewsBackgroundImage
    form_class = NewsBackgroundImagery
    template_name = "newsbackgroundimagechange.html"
    success_url = reverse_lazy("newsfeed")


class UploadACardView(FormMixin, LoginRequiredMixin, ListView):
    model = UploadACard
    template_name = "makeacard.html"
    form_class = UploadCardsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        return context

    # @login_required
    def post(self, request, *args, **kwargs):
        form = UploadCardsForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('showcase:index')
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "makeacard.html", {'form': form})


class DonorView(BaseView):
    model = DonorBackgroundImage
    template_name = "donors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        # context['BaseHomeTexted'] = BaseHomeText.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context

    def dispatch(self, request, *args, **kwargs):
        # Check if there is a signed-in user
        if request.user.is_authenticated:
            user = request.user
            print(user)
        else:
            # If no signed-in user, use a default user or None as desired
            user = None  # Or use default_user if it is previously defined

        # Continue with the regular flow, passing the determined user to the view
        return super().dispatch(request, *args, user=user, **kwargs)


class ContributorBackgroundView(BaseView):
    model = ContributorBackgroundImage
    template_name = "contributors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        return context


class ContentBackgroundView(BaseView):
    model = ContentBackgroundImage
    template_name = "morecontent.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ContentBackgroundImage'] = ContentBackgroundImage.objects.all()
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        return context


class PartnerBackgroundView(BaseView):
    model = PartnerBackgroundImage
    template_name = "partners.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['PartnerBackgroundImage'] = PartnerBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Partner'] = PartnerApplication.objects.all()

        newprofile = PartnerApplication.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class ShareBackgroundView(BaseView):
    model = ShareBackgroundImage
    template_name = "share.html"

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')

            return render(request, "emaildone.html", {'form': form})
            # return redirect('showcase:emaildone')  # possibly change to a finished email registration page
        else:
            messages.error(request, "Form submission invalid")
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            return render(request, "share.html", {'form': form})
            return redirect('showcase:share')

    def get(self, request, *args, **kwargs):
        form = EmailForm()
        self.object_list = self.get_queryset()  # Add this line
        context = self.get_context_data(**kwargs)  # Call get_context_data here
        return render(request, "share.html", {'form': form, **context})

    def get_queryset(self):
        return ShareBackgroundImage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Ideas'] = Idea.objects.all()

        newprofile = Idea.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


class ConvertBackgroundView(BaseView):
    model = ConvertBackgroundImage
    template_name = "convert.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ConvertBackgroundImage'] = ConvertBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        return context


class ReasonsBackgroundView(BaseView):
    model = ReasonsBackgroundImage
    template_name = "reasons-to-convert.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ConvertBackgroundImage'] = ConvertBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        return context


class PerksBackgroundView(BaseView):
    model = PerksBackgroundImage
    template_name = "perks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ShowcaseBackgroundImage'] = ShowcaseBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['TextFielde'] = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")
        return context


#  def get_queryset(self):
#    return BackgroundImage.objects.all()

#  def get_context_data(request):
#    images = os.listdir("static/css/images") #Can use glob as well
#    context = {'images': images}
#    return render(request,'/home/runner/PokeTrove-Attempt-Backedmore/templates',context)

# class Background2aView(ListView):
#  model = Background2aImage
#  paginate_by = 10
#  template_name = 'index.html'
#  extra_context = {'Background2aIm
#  age.url': Background2aImage.objects.all()[0].get_absolute_url()}

#  def get_queryset(self):
#    return Background2aImage.objects.all()


def home(request):
    return render(request, 'home.html')


from django.http import HttpRequest, JsonResponse
from django.views.generic import TemplateView

from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import JsonResponse
from django.views import View
from django.core import serializers

"""
def get_profile_url(message):
   return f"http://127.0.0.1:8000/profile/{message.signed_in_user_id}/"
"""
from django.http import JsonResponse

from django.shortcuts import get_object_or_404


def supportgetMessages(request, signed_in_user, **kwargs):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return JsonResponse({'messages': []})

    try:
        chat_room = SupportChat.objects.get(signed_in_user__username=signed_in_user)
    except SupportChat.DoesNotExist:
        # Create a new chat room if it doesn't exist
        chat_room = SupportChat(signed_in_user=request.user)
        chat_room.save()

    # Check if the requesting user is the creator of the room or an administrator
    if request.user == chat_room.signed_in_user or request.user.is_staff:
        messages = SupportMessage.objects.filter(room=chat_room)
        messages_data = []

        for message in messages:
            user_str = str(message.signed_in_user) if message.signed_in_user else 'Support Request'
            user_profile_url = ''  # Initialize user_profile_url
            profile_details = ProfileDetails.objects.filter(user=message.signed_in_user).first()

            if message.signed_in_user and profile_details:
                user_profile_url = profile_details.get_absolute_url()  # Get the user_profile_url for each message
            if profile_details:
                avatar_url = profile_details.avatar.url  # Get the avatar URL
            else:
                avatar_url = staticfiles_storage.url('css/images/a.jpg')  # Default avatar URL

            messages_data.append({
                'user_profile_url': user_profile_url,
                'avatar_url': avatar_url,
                'user': user_str,
                'value': message.value,
                'date': message.date.strftime("%Y-%m-%d %H:%M:%S"),
            })

        return JsonResponse({'messages': messages_data})
    else:
        return HttpResponseForbidden("You do not have permission to access this chat room")



"""def supportgetMessages(request, **kwargs):
   messages = SupportMessage.objects.filter(room=request.user.username)
   return JsonResponse({"messages": list(messages.values())})
"""

# class post(ListView):
#  template_name = 'users.html'


"""@login_required
def poste(request):
  if (request.method == "POST"):
      form = Postit(request.POST)
      if (form.is_valid()):
          post = form.save(commit=False)
          post.save()
          return redirect('showcase:users')
  else:
      form = Postit()
      return render(request, 'share.html', {'form': form})
      messages.error(
          request, 'Form submission failed to register, please try again.')
      messages.error(request, form.errors)"""

"""class PostBackgroundView(FormMixin, ListView):
   model = UpdateProfile
   template_name = "post_edit.html"
   form_class = PostForm

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
       context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
       context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
           "position")
       # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
       context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
       return context
"""


# @login_required


class PostView(FormMixin, ListView):
    model = PostBackgroundImage
    template_name = "ideas.html"
    form_class = Postit
    queryset = PostBackgroundImage.objects.all()  # Add this line

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ShareBackgroundImage'] = ShareBackgroundImage.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Idea'] = Idea.objects.all()
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = Postit(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                form.instance.user = request.user
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:share')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "ideas.html", {'form': form})
        else:
            form = Postit()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "ideas.html", {'form': form})


"""@login_required
def post_new(request):
  if (request.method == "POST"):
      form = PostForm(request.POST)
      if (form.is_valid()):
          post = form.save(commit=False)
          post.save()
          return redirect('showcase:showcase')
          messages.success(request, 'Form submitted successfully.')
      else:
          messages.error(request, "Form submission invalid")
          return render(request, "post_edit.html", {'form': form})
  else:
      form = PostForm()
      return render(request, "post_edit.html", {'form': form})
      messages.error(
          request, 'Form submission failed to register, please try again.')
      messages.error(request, form.errors)"""


class Title(ListView):
    model = Titled

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        return render(context)


class DonateIconView(ListView):
    model = DonateIcon
    template_name = "donatebase.html"


class SupportBackgroundView(FormMixin, ListView):
    model = Support
    template_name = "support.html"
    form_class = SupportForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SupportBackgroundImage'] = SupportBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Support'] = Support.objects.all()
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = SupportForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                print('works')
                messages.success(request, 'Form submitted successfully.')
                return HttpResponse('Support ticket generated')
                return redirect('showcase:showcase')
            else:
                messages.error(request, "Form submission invalid")
                return render(request, "support.html", {'form': form})
                return HttpResponse('Form submission invalid.')
        else:
            form = SupportForm()
            return render(request, "support.html", {'form': form})
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return HttpResponse('Form submission failed to register, please try again.')


class PostingView(FormMixin, ListView):
    model = UpdateProfile
    template_name = "post_edit.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Profile'] = UpdateProfile.objects.all()
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()

        newprofile = UpdateProfile.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                form.instance.user = request.user
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:showcase')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "post_edit.html", {'form': form})
        else:
            form = PostForm()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "post_edit.html", {'form': form})


from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import PollQuestion

# Get questions and display them


from django.shortcuts import render
from django.views import View
from .models import PollQuestion


class PollQuestionsView(View):
    template_name = "pollquestions.html"

    def get_context_data(self, **kwargs):
        context = {
            'Background': BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'PostBackgroundImage': PostBackgroundImage.objects.all(),
            'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
            'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
            'DropDown': NavBar.objects.filter(is_active=1).order_by('position'),
            'Logo': LogoBase.objects.filter(page=self.template_name, is_active=1),
        }
        return context

    def get(self, request, *args, **kwargs):
        # Retrieve the latest poll questions
        latest_question_list = PollQuestion.objects.order_by('-pub_date')[:5]

        # Populate the context
        context = {
            'latest_question_list': latest_question_list,
            'object_list': latest_question_list  # Add this for the generic view
        }

        # Add additional context data
        context.update(self.get_context_data())

        # Render the template with the context
        return render(request, self.template_name, context)


def polldetail(request, question_id):
    try:
        question = PollQuestion.objects.get(pk=question_id)
    except PollQuestion.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polldetail.html', {'question': question})


class PollDetailView(TemplateView):
    template_name = 'polldetail.html'

    def get_context_data(self, **kwargs):
        question_id = self.kwargs.get('question_id')
        question = get_object_or_404(PollQuestion, pk=question_id)

        context = {
            'question': question,
            'Background': BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'PostBackgroundImage': PostBackgroundImage.objects.all(),
            'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
            'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
            'DropDown': NavBar.objects.filter(is_active=1).order_by('position'),
            'Logo': LogoBase.objects.filter(page=self.template_name, is_active=1),
        }
        return context


class PollResultsView(View):
    template_name = 'pollresults.html'  # specify your template name here

    def get(self, request, question_id):
        context = self.get_context_data(question_id)
        return render(request, self.template_name, context)

    def get_context_data(self, question_id):
        question = get_object_or_404(PollQuestion, pk=question_id)
        context = {
            'question': question,
            'Background': BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'PostBackgroundImage': PostBackgroundImage.objects.all(),
            'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
            'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
            'DropDown': NavBar.objects.filter(is_active=1).order_by('position'),
            'Logo': LogoBase.objects.filter(page=self.template_name, is_active=1),
        }
        return context


# Vote for a question choice

class PollingView(View):
    model = Choice
    template_name = "pollvote.html"

    def post(self, request, *args, **kwargs):
        question_id = self.kwargs.get('question_id')
        question = get_object_or_404(PollQuestion, pk=question_id)

        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            error_message = "You did not select a choice."
            context = {
                'question': question,
                'error_message': error_message,
                'Background': BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
                    "position"),
                'PostBackgroundImage': PostBackgroundImage.objects.all(),
                'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
                'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
                'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
                'DropDown': NavBar.objects.filter(is_active=1).order_by('position')
            }
            return render(request, self.template_name, context)
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('showcase:pollresults', args=(question.id,)))


class InventoryView(FormMixin, ListView):
    model = PrizePool
    template_name = "pokespinner.html"
    form_class = PosteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['PrizePool'] = PrizePool.objects.all()
        context['Shuffle'] = Shuffler.objects.filter(is_active=1).order_by("category")
        return context

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.db import transaction
from django.urls import reverse


class PlayerInventoryView(LoginRequiredMixin, FormMixin, ListView):
    model = InventoryObject
    template_name = "inventory.html"
    form_class = AddTradeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Stockpile'] = Inventory.objects.filter(is_active=1, user=self.request.user)
        try:
            context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            context['SentProfile'] = None
        context['Money'] = Currency.objects.filter(is_active=1)
        context['StockObject'] = InventoryObject.objects.filter(is_active=1, user=self.request.user)
        context['TradeItems'] = TradeItem.objects.filter(is_active=1, user=self.request.user)
        context['TextFielde'] = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        action = self.request.POST.get('action')
        pk = self.request.POST.get('pk')

        if action == 'sell':
            return self.sell_inventory_object(request, pk)
        elif action == 'withdraw':
            return self.withdraw_inventory_object(request, pk)
        elif action == 'move':
            return self.move_to_trade(request, pk)
        else:
            return HttpResponse(status=400)  # Bad request if action is unknown

    def withdraw_inventory_object(self, request, pk):
        inventory_object = get_object_or_404(InventoryObject, pk=pk)

        # Check if user owns the inventory object
        if inventory_object.user != request.user:
            messages.error(request, 'You cannot withdraw items you do not own!')
            return redirect('showcase:inventory')

        # Update InventoryObject
        inventory_object.user = None
        inventory_object.inventory = None
        inventory_object.save()

        # Handle withdrawal logic
        user = request.user

        with transaction.atomic():
            # Query for an active withdrawal with fewer than 25 cards
            withdraw = Withdraw.objects.filter(user=user, is_active=1, shipping_state='S', number_of_cards__lt=25).first()

            if withdraw:
                # Update existing withdrawal
                withdraw.cards.add(inventory_object)
            else:
                # Create a new withdrawal
                withdraw = Withdraw.objects.create(user=user, is_active=1, shipping_state='S')
                withdraw.cards.add(inventory_object)

            # Update number of cards after adding the inventory object
            withdraw.number_of_cards = withdraw.cards.count()
            withdraw.save()

        messages.success(request, f"Successfully withdrawn {inventory_object.choice}!")
        return redirect('showcase:inventory')  # Ensure the redirect URL is correct

    def sell_inventory_object(self, request, pk):
        inventory_object = get_object_or_404(InventoryObject, pk=pk)

        # Check if user owns the inventory object
        if inventory_object.user != request.user:
            messages.error(request, 'You cannot sell items you do not own!')
            return redirect('showcase:inventory')

        # Update InventoryObject
        inventory_object.user = None
        inventory_object.inventory = None

        with transaction.atomic():
            # Create the Transaction instance
            Transaction.objects.create(
                inventory_object=inventory_object,
                user=request.user,
                currency=inventory_object.currency,
                amount=inventory_object.price
            )

            # Save the updated InventoryObject
            inventory_object.save()

            # Update UserProfile's currency_amount
            user_profile = get_object_or_404(UserProfile, user=request.user)
            user_profile.currency_amount += inventory_object.price
            user_profile.save()

        messages.success(request, f"Successfully sold {inventory_object.choice} for {inventory_object.price} {inventory_object.currency}!")
        return redirect('showcase:inventory')


    def move_to_trade(self, request, pk):
        inventory_item = get_object_or_404(InventoryObject, pk=pk, user=request.user)

        if request.method == 'POST':
            form = MoveToTradeForm(request.POST, request.FILES)
            if form.is_valid():
                trade_item = inventory_item.move_to_trading(
                    title=form.cleaned_data['title'],
                    fees=form.cleaned_data['fees'],
                    category=form.cleaned_data['category'],
                    specialty=form.cleaned_data['specialty'],
                    condition=form.cleaned_data['condition'],
                    label=form.cleaned_data['label'],
                    slug=form.cleaned_data['slug'],
                    description=form.cleaned_data['description'],
                    image=form.cleaned_data['image'],
                    image_length=form.cleaned_data['image_length'],
                    image_width=form.cleaned_data['image_width'],
                    length_for_resize=form.cleaned_data['length_for_resize'],
                    width_for_resize=form.cleaned_data['width_for_resize']
                )
                return redirect('showcase:tradeitem_detail', trade_item.id)  # Redirect to the TradeItem detail view
        else:
            form = MoveToTradeForm()

        return render(request, 'inventory.html', {'form': form, 'inventory_item': inventory_item})

    def remove_trade_object(self, request, pk):
        trade_item = get_object_or_404(TradeItem, pk=pk)

        if trade_item.user != request.user:
            messages.error(request, 'You cannot remove tradable items you do not own!')
            return redirect('showcase:tradeinventory')

        trade_item.user = None
        trade_item.inventory = None
        trade_item.save()

        messages.success(request, f"Successfully removed {trade_item.title}!")
        return redirect('showcase:tradeinventory')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CreateChestView(FormView):
    template_name = "create_chest.html"
    form_class = GameForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['game_form'] = GameForm(self.request.POST, self.request.FILES)
            context['formset'] = ChoiceFormSet(self.request.POST, self.request.FILES)
        else:
            context['game_form'] = GameForm()
            context['formset'] = ChoiceFormSet()

        # Add other context data as needed
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['PrizePool'] = PrizePool.objects.all()
        context['Shuffle'] = Shuffler.objects.filter(is_active=1).order_by("category")
        return context

    def post(self, request, *args, **kwargs):
        game_form = GameForm(request.POST, request.FILES)
        formset = ChoiceFormSet(request.POST, request.FILES)

        if not game_form.is_valid():
            print("Game Form Errors:", game_form.errors)
        if not formset.is_valid():
            print("Formset Management Form:", formset.management_form.errors)
            for form in formset:
                print("Form errors:", form.errors)

        if game_form.is_valid() and formset.is_valid():
            game = game_form.save()
            choices = formset.save(commit=False)
            for choice in choices:
                choice.game = game
                choice.save()
            return redirect('game_detail', pk=game.pk)  # Adjust redirect as needed
        else:
            return self.render_to_response(self.get_context_data(game_form=game_form, formset=formset))



@login_required
def move_to_trade(request, inventory_id):
    inventory_item = get_object_or_404(Inventory, id=inventory_id, user=request.user)

    if request.method == 'POST':
        form = MoveToTradeForm(request.POST, request.FILES)
        if form.is_valid():
            trade_item = inventory_item.move_to_trading(
                title=form.cleaned_data['title'],
                fees=form.cleaned_data['fees'],
                category=form.cleaned_data['category'],
                specialty=form.cleaned_data['specialty'],
                condition=form.cleaned_data['condition'],
                label=form.cleaned_data['label'],
                slug=form.cleaned_data['slug'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image'],
                image_length=form.cleaned_data['image_length'],
                image_width=form.cleaned_data['image_width'],
                length_for_resize=form.cleaned_data['length_for_resize'],
                width_for_resize=form.cleaned_data['width_for_resize']
            )
            return redirect('showcase:tradeinventory')  # Redirect to the TradeItem detail view

    else:
        form = MoveToTradeForm()

    return render(request, 'inventory.html', {'form': form, 'inventory_item': inventory_item})


from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from .models import Game, Choice
from .forms import GameForm, ChoiceFormSet
from django.shortcuts import render, redirect
from .models import Game, Choice
from .forms import GameForm, ChoiceFormSet


class SecretRoomView(LoginRequiredMixin, FormMixin, ListView):
    model = SecretRoom
    template_name = "secretrooms.html"
    form_class = PosteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Stockpile'] = Inventory.objects.filter(is_active=1, user=self.request.user)
        context['SentProfile'] = UserProfile.objects.get(user=self.request.user)
        context['Money'] = Currency.objects.filter(is_active=1)
        context['StockObject'] = InventoryObject.objects.filter(is_active=1, user=self.request.user)
        context['TradeItems'] = TradeItem.objects.filter(is_active=1, user=self.request.user)
        context['TextFielde'] = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")
        return context


@login_required
def delete_trade_item(request, item_id):
    trade_item = get_object_or_404(TradeItem, id=item_id)
    if trade_item.user == request.user:
        trade_item.delete()
        messages.success(request, 'Trade item deleted successfully.')
        return redirect('showcase:tradeinventory')
    else:
        messages.error(request, 'You do not have permission to delete this item.')
        return redirect('showcase:tradeinventory')


class TradeInventoryView(LoginRequiredMixin, FormMixin, ListView):
    model = InventoryObject
    template_name = "tradeinventory.html"
    form_class = PosteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Stockpile'] = Inventory.objects.filter(is_active=1, user=self.request.user)
        context['StockObject'] = InventoryObject.objects.filter(is_active=1, user=self.request.user)
        context['TradeItems'] = TradeItem.objects.filter(is_active=1, user=self.request.user)
        context['TextFielde'] = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")
        return context

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        action = self.request.POST.get('action')
        pk = self.request.POST.get('pk')

        if action == 'remove':
            return self.remove_trade_object(request, pk)

        # If no action matches, return an appropriate response
        return HttpResponse(status=400)

    def remove_trade_object(self, request, pk):
        trade_item = get_object_or_404(TradeItem, pk=pk)

        if trade_item.user != request.user:
            messages.error(request, 'You cannot remove tradable items you do not own!')
            return redirect('showcase:tradeinventory')

        trade_item.delete()
        messages.success(request, f"Successfully removed {trade_item.title}!")
        return redirect('showcase:tradeinventory')


from .models import LotteryTickets, Lottery
from .forms import TicketRequestForm


class LotteryBackgroundView(BaseView):
    model = Lottery
    template_name = "lotteries.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ShowcaseBackgroundImage'] = ShowcaseBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        context['Lotto'] = Lottery.objects.filter(is_active=1)

        return context


class DailyLotteryView(FormMixin, ListView):
    model = Lottery
    template_name = "dailylotto.html"
    form_class = TicketRequestForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Profile'] = UpdateProfile.objects.all()

        newprofile = UpdateProfile.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = TicketRequestForm(request.POST, user=request.user)  # Pass user=request.user
        if form.is_valid():
            post = form.save(commit=False)
            lottery, created = Lottery.objects.get_or_create(
                name__in=['Daily Lotto', 'Daily Lottery'],
                defaults={'name': 'Daily Lotto', 'flavor_text': 'Your daily chance to win!'}
            )
            lottery.save()  # Save the lottery object to the database
            post.lottery = lottery
            post.user = request.user  # Set the user attribute
            post.save()
            return redirect('showcase:dailylottoclaimed')
        else:
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            messages.error(request, 'You need to log in to claim your daily ticket!')
            return render(request, 'registration/login.html', {'form': form})


class Lottereal(BaseView):
    model = Lottery
    template_name = "lotteries.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Vote'] = Vote.objects.all()
        return context


class PosteView(FormMixin, ListView):
    model = VoteBackgroundImage
    template_name = "vote.html"
    form_class = PosteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Vote'] = Vote.objects.all()
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = PosteForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                form.instance.user = request.user
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:voting')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "vote.html", {'form': form})
        else:
            form = PostForm()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "vote.html", {'form': form})


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'


@method_decorator(login_required, name='dispatch')
class TradeOffersView(View):
    def get(self, request, *args, **kwargs):
        # Get all pending friend requests for the current user
        pending_requests = TradeOffer.objects.select_related('trade_items').filter(user2=request.user,
                                                                                   status=TradeOffer.PENDING)
        outgoing_requests = TradeOffer.objects.filter(user=request.user, status=TradeOffer.PENDING)

        context = {}
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        current_user = self.request.user

        newprofile = TradeOffer.objects.filter(user=request.user, is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        if is_ajax(request):
            context.update({'pending_requests': pending_requests, 'outgoing_requests': outgoing_requests})
            return render(request, 'pendingtrades.html', context)

        context.update({'pending_requests': pending_requests, 'outgoing_requests': outgoing_requests})
        return render(request, 'pendingtrades.html', context)


from django.http import JsonResponse


@method_decorator(login_required, name='dispatch')
class DirectedTradeOfferView(View):

    def is_ajax(self, request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get(self, request, *args, **kwargs):
        # Get all pending friend requests for the current user
        pending_requests = TradeOffer.objects.filter(user2=request.user, trade_status=TradeOffer.PENDING)
        outgoing_requests = TradeOffer.objects.filter(user=request.user, trade_status=TradeOffer.PENDING)

        response_pending_requests = RespondingTradeOffer.objects.filter(user2=request.user,
                                                                        trade_status=RespondingTradeOffer.PENDING)
        response_outgoing_requests = RespondingTradeOffer.objects.filter(user=request.user,
                                                                         trade_status=RespondingTradeOffer.PENDING)

        context = {}
        context.update({
            'pending_requests': pending_requests,
            'outgoing_requests': outgoing_requests,
            'response_pending_requests': response_pending_requests,
            'response_outgoing_requests': response_outgoing_requests
        })
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['request'] = request  # Pass the request object to the context
        current_user = request.user

        newprofile = TradeOffer.objects.filter(user=current_user.id, is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        responsetradeoffers = RespondingTradeOffer.objects.filter(user=self.request.user, is_active=1)
        context['ResponseTrade'] = responsetradeoffers
        for responsetradeoffer in context['ResponseTrade']:
            user = responsetradeoffer.user
            if user:
                responsetradeoffer.responsetradeoffer_trade_url = responsetradeoffer.get_profile_url2()

        if self.is_ajax(request):
            context.update({'pending_requests': pending_requests, 'outgoing_requests': outgoing_requests})
            return render(request, 'directedtradeoffers.html', context)

        context.update({'pending_requests': pending_requests, 'outgoing_requests': outgoing_requests})
        return render(request, 'directedtradeoffers.html', context)


@login_required
def accept_trade(request, request_id):
    trade_offer = get_object_or_404(TradeOffer, id=request_id)
    print('trade offer acceptance')
    if request.user != trade_offer.user2 or not trade_offer.user2:
        raise PermissionDenied
    trade_offer.trade_status = TradeOffer.ACCEPTED
    trade_offer.save()
    messages.success(request, 'You have accepted the trade offer.')
    return redirect('showcase:mytrades')


@login_required
def decline_trade(request, request_id):
    trade_offer = get_object_or_404(TradeOffer, id=request_id)
    if request.user != trade_offer.user2 or not trade_offer.user2:
        raise PermissionDenied
    trade_offer.trade_status = TradeOffer.DECLINED
    trade_offer.save()
    messages.success(request, 'You have declined the trade offer.')
    return redirect('showcase:mytrades')


@login_required
def accept_response_trade(request, request_id):
    trade_offer = get_object_or_404(RespondingTradeOffer, id=request_id)

    # Check user permissions
    if request.user != trade_offer.user2 or not trade_offer.user2:
        raise PermissionDenied

    # Update the responding trade offer status
    RespondingTradeOffer.objects.filter(id=request_id).update(trade_status=RespondingTradeOffer.ACCEPTED)

    # Create a new Trade object and establish relationships if necessary
    wanted_trade_offer = trade_offer.wanted_trade_items
    if wanted_trade_offer and not Trade.objects.filter(trade_offers__in=[wanted_trade_offer]).exists():
        trade = Trade.objects.create()
        trade.trade_offers.add(wanted_trade_offer)
        trade.users.add(trade_offer.user, trade_offer.user2)

    messages.success(request, 'You have accepted the trade offer.')
    return redirect('showcase:mytrades')


@login_required
def decline_response_trade(request, request_id):
    trade_offer = get_object_or_404(RespondingTradeOffer, id=request_id)
    if request.user != trade_offer.user2 or not trade_offer.user2:
        raise PermissionDenied
    trade_offer.trade_status = RespondingTradeOffer.DECLINED
    trade_offer.save()
    messages.success(request, 'You have declined the trade offer.')
    return redirect('showcase:mytrades')


class TradeHistory(ListView):
    model = Trade
    template_name = "mytrades.html"

    def get_context_data(self, **kwargs):

        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Feed'] = Feedback.objects.filter(is_active=1, feedbackpage=self.template_name).order_by("slug")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        current_user = self.request.user
        user_trades = Trade.objects.filter(users=current_user)
        context['user_trades'] = user_trades
        context['feedback'] = Feedback.objects.all()
        # context['orders'] = OrderItem.objects.filter(user=self.request.user)
        print(user)

        # Retrieve the author's profile avatar
        items = TradeItem.objects.filter(is_active=1)

        context['Iteme'] = items

        # Iterate over each item in 'Iteme'
        for items in context['Iteme']:
            # Get the image of the item
            image = items.image
            # Check if the user is authenticated
            if user.is_authenticated:
                # Try to get the first profile detail of the current user
                profile = ProfileDetails.objects.filter(user=user).first()
                # If a profile detail exists
                if profile:
                    # Update the author's profile picture URL in the item
                    items.author_profile_picture_url = profile.avatar.url
                    # Update the author's profile URL in the item
            else:
                # Handle the case when the user is not authenticated
                messages.warning(self.request, "You need to log in")
                return redirect("accounts/login")  # replace "login" with your login route

        current_user = self.request.user
        user_trades = Trade.objects.filter(is_active=1, users=current_user)
        total_items = OrderItem.objects.filter(is_active=1).count()

        # Get the paginate_by value from the form data or settings
        paginate_by = int(self.request.GET.get('paginate_by', settings.DEFAULT_PAGINATE_BY))

        items_query = Trade.objects.filter(is_active=1)
        paginator = Paginator(items_query, paginate_by)
        page_number = self.request.GET.get('page')
        paginated_items = paginator.get_page(page_number)

        # context['items'] = paginated_items

        # context['items'] = Item.objects.filter(is_active=1)

        context['orders'] = paginated_items
        for order_item in context['orders']:
            # Process each order item individually
            user = self.request.user
            profile = ProfileDetails.objects.filter(user=user).first()  # Fetch the profile for the current user

            order_item.author_profile_url = order_item.get_profile_url() if order_item.get_profile_url() else None
            order_item.hyperlink = order_item.get_profile_url()  # Example, adjust this as needed

            if profile:
                order_item.author_profile_picture_url = profile.avatar.url

        return context


class SettingsView(RegularUserRequiredMixin, UserPassesTestMixin, FormView):
    """Only allow registered users to change their settings."""
    form_class = SettingsForm
    model = SettingsModel
    template_name = "myaccount.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_settings = self.request.user.settings

        context['username'] = self.request.user.username
        context['password'] = SettingsModel.password
        context['email'] = SettingsModel.email
        context['coupons'] = SettingsModel.coupons
        context['news'] = SettingsModel.news
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        # context['name'] = Showcase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        return context

    def test_func(self):
        return self.request.user.is_superuser


from django.contrib.messages.views import SuccessMessageMixin


class SettingsBackgroundView(SuccessMessageMixin, FormView):
    model = SettingsBackgroundImage
    form_class = SettingsForm
    template_name = "settings.html"
    success_url = reverse_lazy('showcase:myaccount')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        print(FaviconBase.objects.all())
        context['SettingsBackgroundView'] = self.model.objects.all()
        return context

    # @RegularUserRequiredMixin
    # @login_required

    from django.db import transaction

    @transaction.atomic
    def form_valid(self, form):
        user = self.request.user
        settings_model, _ = SettingsModel.objects.get_or_create(user=user)

        # Check if the new username conflicts with existing usernames
        new_username = form.cleaned_data['username']
        if User.objects.filter(username=new_username).exclude(pk=user.pk).exists():
            messages.error(self.request, 'Username already exists. Please choose a different username.')
            return self.form_invalid(form)

        # Update the user's username and password based on the SettingsModel
        user.username = new_username
        user.set_password(form.cleaned_data['password'])
        new_email = form.cleaned_data['email']
        user.email = new_email
        user.save()

        # Update the SettingsModel with the new form data
        settings_model.email = form.cleaned_data['email']
        settings_model.coupons = form.cleaned_data['coupons']
        settings_model.news = form.cleaned_data['news']
        settings_model.save()

        return super().form_valid(form)


class HomePageView(TemplateView):
    template_name = 'index.html'


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class EcommerceSearchResultsView(ListView):
    model = Item
    template_name = 'ecommercesearch_results.html'

    def get_queryset(self):
        print(1234)
        query = self.request.GET.get('q')
        item_list = Item.objects.filter(
            Q(title__icontains=query) | Q(slug__icontains=query))

        all_list = {
            "item_list": item_list,
        }
        print(234)
        print(all_list)

        return (all_list)


class BlogSearchResultsView(ListView):
    template_name = 'blogsearch_results.html'
    paginate_by = 10
    context_object_name = 'all_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        filter_by = self.request.GET.get('filter')  # Get the filter parameter

        # Define the lists to search based on the filter parameter
        search_lists = []

        if filter_by == 'blog':
            search_lists.append(Blog.objects.filter(
                Q(title__icontains=query) | Q(slug__icontains=query) | Q(type__icontains=query) | Q(
                    author__username__icontains=query)))
        elif filter_by == 'blogfilter':
            search_lists.append(BlogFilter.objects.filter(
                Q(blog_filter__icontains=query)))
        elif filter_by == 'blogheader':
            search_lists.append(BlogHeader.objects.filter(
                Q(category__icontains=query)))
        else:
            search_lists = [Blog.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query) |
                                                Q(type__icontains=query) | Q(author__username__icontains=query)),
                            BlogFilter.objects.filter(Q(blog_filter__icontains=query)),
                            BlogHeader.objects.filter(Q(category__icontains=query))]

        # Combine the search results from selected lists
        search_results = []
        for search_list in search_lists:
            for item in search_list:
                search_result = SearchResult(content_object=item)
                search_results.append(search_result)

        return search_results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        # settings to alter the username & password

        # Add type information for each item
        for result in context['all_list']:
            if isinstance(result.content_object, Blog):
                result.type = 'Blog'
                result.url = reverse_lazy('showcase:blog')
            elif isinstance(result.content_object, BlogFilter):
                result.type = 'BlogFilter'
                result.url = reverse_lazy('showcase:blog')
            elif isinstance(result.content_object, BlogHeader):
                result.type = 'Blog Header'
                result.url = reverse_lazy('showcase:blog')
            else:
                result.type = 'Unknown'
                result.url = ''

        return context


class GameCategorySearchResultsView(ListView):
    model = GameHub
    template_name = 'gamehubsearchresults.html'

    def get_queryset(self):
        print(1234)
        query = self.request.GET.get('q')
        game_category_list = GameHub.objects.filter(
            Q(name__icontains=query) | Q(slug__icontains=query))

        all_list = {
            "game_category_list": game_category_list,
        }
        print(234)
        print(all_list)

        return (all_list)


class GameSearchResultsView(ListView):
    model = Game
    template_name = 'gamesearchresults.html'

    def get_queryset(self):
        print(1234)
        query = self.request.GET.get('q')
        game_list = Game.objects.filter(
            Q(name__icontains=query) | Q(slug__icontains=query))

        all_list = {
            "game_list": game_list,
        }
        print(234)
        print(all_list)

        return (all_list)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)

        newprofile = Game.objects.filter(is_active=1)
        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context

from django.views.generic import ListView
from django.db.models import Q
from showcase.models import City, Vote, UpdateProfile, Idea, PartnerApplication, SearchResult


class SearchResultsView(ListView):
    template_name = 'search_results.html'
    paginate_by = 10
    context_object_name = 'all_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        filter_by = self.request.GET.get('filter')  # Get the filter parameter

        # Define the lists to search based on the filter parameter
        search_lists = []

        if filter_by == 'city':
            search_lists.append(City.objects.filter(Q(name__icontains=query) | Q(state__icontains=query)))
        elif filter_by == 'vote':
            search_lists.append(Vote.objects.filter(
                Q(name__icontains=query) | Q(category__icontains=query) | Q(description__icontains=query)))
        elif filter_by == 'profile':
            search_lists.append(UpdateProfile.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query) | Q(image__icontains=query)))
        elif filter_by == 'idea':
            search_lists.append(Idea.objects.filter(
                Q(name__icontains=query) | Q(category__icontains=query) | Q(description__icontains=query) | Q(
                    image__icontains=query)))
        elif filter_by == 'partner':
            search_lists.append(PartnerApplication.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query) | Q(server_invite__icontains=query)))
        elif filter_by == 'news':
            search_lists.append(NewsFeed.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query) | Q(slug__icontains=query)))
        else:
            # If no filter is specified, search all lists
            search_lists = [City.objects.filter(Q(name__icontains=query) | Q(state__icontains=query)),
                            Vote.objects.filter(Q(name__icontains=query) | Q(category__icontains=query) | Q(
                                description__icontains=query)),
                            UpdateProfile.objects.filter(
                                Q(name__icontains=query) | Q(description__icontains=query) | Q(image__icontains=query)),
                            Idea.objects.filter(Q(name__icontains=query) | Q(category__icontains=query) | Q(
                                description__icontains=query) | Q(image__icontains=query)),
                            PartnerApplication.objects.filter(
                                Q(name__icontains=query) | Q(description__icontains=query) | Q(
                                    server_invite__icontains=query)),
                            NewsFeed.objects.filter(
                                Q(name__icontains=query) | Q(description__icontains=query) | Q(slug__icontains=query))]

        # Combine the search results from selected lists
        search_results = []
        for search_list in search_lists:
            for item in search_list:
                search_result = SearchResult(content_object=item)
                search_results.append(search_result)

        return search_results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        # settings to alter the username & password

        # Add type information for each item
        for result in context['all_list']:
            if isinstance(result.content_object, City):
                result.type = 'City'
                result.url = ''
            elif isinstance(result.content_object, Vote):
                result.type = 'Vote'
                result.url = reverse_lazy('showcase:voting')
            elif isinstance(result.content_object, UpdateProfile):
                result.type = 'Profile'
                result.url = reverse_lazy('showcase:showcase')
            elif isinstance(result.content_object, Idea):
                result.type = 'Idea'
                result.url = reverse_lazy('showcase:share')
            elif isinstance(result.content_object, PartnerApplication):
                result.type = 'Partner'
                result.url = reverse_lazy('showcase:partners')
            elif isinstance(result.content_object, NewsFeed):
                result.type = 'News'
                result.url = reverse_lazy('showcase:newsfeed')
            else:
                result.type = 'Unknown'
                result.url = ''

        return context


class PageSearchResultsView(ListView):
    model = NavBar
    template_name = 'index.html'

    def get_queryset(self):
        query = self.request.GET.get('search_query')
        search_type = self.request.GET.get('search_type')
        search_lists = []

        if search_type == "text":
            nav_list = NavBar.objects.filter(
                Q(text__icontains=query))
        elif search_type == "url":
            if query.startswith(("http://", "https://")):
                # Try to extract the path from the URL
                url_path = urllib.parse.urlparse(query).path
                nav_list = NavBar.objects.filter(url__icontains=url_path)
            else:
                # Handle invalid URL format
                nav_list = None  # Or display an error message
        else:
            # Handle invalid search type
            nav_list = None

        all_list = {
            "nav_list": nav_list,
        }
        return all_list

    def post(self, request, *args, **kwargs):
        search_query = request.POST.get('search_query')
        search_type = request.POST.get('search_type')

        if search_type == "text":
            nav_list = NavBar.objects.filter(
                Q(text__icontains=search_query))
        elif search_type == "url":
            # Handle URL search (you might need additional logic here)
            if query.startswith(("http://", "https://")):
                # Try to extract the path from the URL
                url_path = urllib.parse.urlparse(query).path
                nav_list = NavBar.objects.filter(url__icontains=url_path)
            else:
                # Handle invalid URL format (optional: display error message)
                nav_list = None
        else:
            # Handle invalid search type (optional: display error message)
            nav_list = None

        if nav_list:  # If a matching navbar item is found
            redirect_url = nav_list.first().url
            return redirect(redirect_url)  # Redirect to the URL
        else:
            # No matching results found (optional: display message)
            return render(request, 'search_results.html',
                          {'message': 'No matching results found.'})  # Render search results template

    def get(self, request, *args, **kwargs):
        # Handle GET requests (for initial search and potential redirection)
        response = super().get(request, *args, **kwargs)  # Get search results
        context = response.context  # Access the context data

        if context['nav_list']:  # If a matching navbar item is found
            # Get the URL from the first matching navbar item
            redirect_url = context['nav_list'].first().url
            return redirect(redirect_url)  # Redirect to the URL
        else:
            # Handle no matching results (display message or keep default behavior)
            return response  # Return the original response (search results)


class CreateWithdrawView(LoginRequiredMixin, CreateView):
    model = Withdraw
    form_class = WithdrawForm
    template_name = "create_withdraw.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def my_cards(request):
        if request.user.is_authenticated:
            # Filter Withdraws where the current user is included and fetch related cards
            withdraws = Withdraw.objects.filter(user=request.user).prefetch_related('cards')
        else:
            withdraws = None  # Handle non-authenticated users (optional)

        context = {'withdraws': withdraws}
        return render(request, 'my_cards.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = WithdrawForm(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                # Assuming 'selected_cards' is a list of selected card IDs from your template
                selected_cards = request.POST.getlist('selected_cards')  # Get selected card IDs from POST data

                # Save the Withdraw instance first (without M2M)
                withdraw = form.save()

                # Now set the selected cards to the 'cards' M2M field
                withdraw.cards.set(selected_cards)

                # Finally, save the complete instance to persist the M2M relation
                withdraw.save()

                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:withdraws')  # Redirect to your desired URL
            else:
                messages.error(request, "Form submission invalid")
                return render(request, "create_withdraw.html", {'form': form})
        else:
            form = WithdrawForm()
            return render(request, "create_withdraw.html", {'form': form})


class WithdrawView(LoginRequiredMixin, ListView):
    model = Withdraw
    template_name = "withdraws.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")

        newprofile = Withdraw.objects.filter(is_active=1)
        # Retrieve the author's profile avatar

        context['Profiles'] = newprofile

        for newprofile in context['Profiles']:
            user = newprofile.user
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                newprofile.newprofile_profile_picture_url = profile.avatar.url
                newprofile.newprofile_profile_url = newprofile.get_profile_url()

        return context


    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Filter completed withdrawals for the current user
            return Withdraw.objects.filter(user=self.request.user)
        else:
            return Withdraw.objects.none()


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import InviteCode
from .forms import InviteCodeForm
from secrets import token_urlsafe

def generate_unique_code(room_name):
  """Generates a unique alphanumeric code with the room name prefix"""
  while True:
    # Generate a random 16-character alphanumeric string
    code_suffix = token_urlsafe(16)
    # Combine room name (if provided) and code suffix with a separator (e.g., underscore)
    code = f"{room_name}_{code_suffix}" if room_name else code_suffix

    # Check for uniqueness in the InviteCode model
    if not InviteCode.objects.filter(code=code).exists():
      return code

@login_required
def generate_invite_link(request):
  if request.method == 'POST':
    form = InviteCodeForm(request.POST)
    if form.is_valid():
      # Generate unique code
      code = generate_unique_code()  # Replace with your code generation function
      invite_code, created = InviteCode.objects.get_or_create(user=request.user, code=code)
      invite_link = f"https://your_app.com/join/{invite_code.code}"
      return render(request, 'invite_link.html', {'invite_link': invite_link})
  else:
    form = InviteCodeForm()
  return render(request, 'generate_invite.html', {'form': form})

# Function to generate a unique random alphanumeric code (replace with your implementation)


# class ProductSearchResultsView(ListView):
#    model = Item
#    template_name = 'search_results.html'

#    def get_queryset(self):
#        query = self.request.GET.get('q')
#        item_list = Item.objects.filter(
#            Q(name__icontains=query) | Q(state__icontains=query)
#        )

#        all_list = {
#           "item_list": item_list,
#       }

#        return (all_list)

from .models import ProfileDetails


# Edit Profile View

class ProfileView(LoginRequiredMixin, UpdateView):
    model = ProfileDetails
    form_class = ProfileForm
    paginate_by = 10
    success_url = reverse_lazy('home')
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # Retrieve the ProfileDetails object based on the captured pk from the URL
        pk = self.kwargs.get('pk')
        return get_object_or_404(ProfileDetails, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['SettingsModel'] = SettingsModel.objects.filter(is_active=1)
        profile = self.get_object()
        context['profile'] = profile
        # settings to alter the username & password
        return context


@login_required
def profile_edit(request, pk):
    profile = get_object_or_404(ProfileDetails, pk=pk)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('showcase:profile_detail', pk=pk)

    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile_edit.html', {'form': form, 'profile': profile})


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('showcase:profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


class StaffJoine(ListView):
    paginate_by = 10
    template_name = 'staffapplication.html'

    def get_queryset(self, *args, **kwargs):
        return StaffApplication.objects.all()


# @RegularUserRequiredMixin
class PunishAppsBackgroundView(FormMixin, ListView):
    model = PunishmentAppeal
    template_name = "punishapps.html"
    form_class = PunishAppeale

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PunishAppsBackgroundImage'] = PunishAppsBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['PunishApps'] = PunishmentAppeal.objects.all()
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = PunishAppeale(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:punishdone')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "punishapps.html", {'form': form})
        else:
            form = PunishAppeale()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "punishapps.html", {'form': form})


class BanAppealBackgroundView(FormMixin, ListView):
    model = BanAppeal
    template_name = "banappeals.html"
    form_class = BanAppeale

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BanAppealBackgroundImage'] = BanAppealBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        context['BanAppeal'] = BanAppeal.objects.all()
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = BanAppeale(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:bandone')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "banappeals.html", {'form': form})
        else:
            form = BanAppeale()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "banappeals.html", {'form': form})


class CommerceExchangeView(CreateView):
    model = CommerceExchange
    template_name = "commerce.html"
    form_class = ExchangePrizesForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        form = ExchangePrizesForm(self.request.POST or None, user=self.request.user)
        context['form'] = form  # Add the form to the context
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        context['form'] = self.get_form()
        return context


class ExchangePrizesView(FormMixin, ListView):
    model = ExchangePrize
    template_name = "commerce.html"
    form = ExchangePrizesForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BanAppealBackgroundImage'] = BanAppealBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(
            is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(
            is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(
            is_active=1).order_by('position')
        context['BanAppeal'] = BanAppeal.objects.all()
        return context


    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = ExchangePrizesForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:commerce')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "commerce.html", {'form': form})
        else:
            form = ExchangePrizesForm()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "commerce.html", {'form': form})


class IssueBackgroundView(FormMixin, ListView):
    model = IssueBackgroundImage
    template_name = "issues.html"
    form_class = ReportIssues

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['IssueBackgroundImage'] = IssueBackgroundImage.objects.all()
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Support'] = Support.objects.all()
        return context

    def usercheck(request):
        try:
            report_issue = ReportIssues.objects.get(user=request.user)
            if report_issue.name.lower() != "anonymous":
                user = request.user
            else:
                user = None
        except ReportIssues.DoesNotExist:
            user = None

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = ReportIssues(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                form.instance.user = request.user
                post.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('showcase:issuedone')
            else:
                print(form.errors)
                print(form.non_field_errors())
                print(form.cleaned_data)
                messages.error(request, "Form submission invalid")
                return render(request, "issues.html", {'form': form})
        else:
            form = ReportIssues()
            messages.error(request, 'Form submission failed to register, please try again.')
            messages.error(request, form.errors)
            return render(request, "issues.html", {'form': form})


# sendemail/views.py


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            print(from_email)
            try:
                send_mail(subject, message, 'intellexcompany1@gmail.com', ['intellexcompany1@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('success')
    print('success')
    # pdb.set_trace()
    return render(request, "email.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


class ContacteView(FormView):
    template_name = 'showcase/email.html'
    form_class = ContactForme
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = 'showcase/email.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(kwargs)
        context["Contact"] = "2123123123123"
        return context


def businessemailcontactView(request):
    if request.method == 'GET':
        form = BusinessContactForm()
    else:
        form = BusinessContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            print(from_email)
            form.save()
            try:
                send_mail(subject, message, from_email, ['intellexcompany1@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('businessemailsuccess')
    print('success')
    # pdb.set_trace()
    return render(request, "businessemail.html", {'form': form})


class BusinessMailingView(FormView):
    template_name = 'businessemail.html'
    form_class = BusinessMailingForm
    success_url = reverse_lazy('showcase:businessmailingsuccess')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        return context

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        form.save()
        return super().form_valid(form)


class BusinessSuccessMailingView(TemplateView):
    template_name = 'businessmailingsuccess.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Contact'] = Contact.objects.all()[len(Contact.objects.all()) - 1]
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        print(context["Contact"])
        context["BusinessMailingContact"] = "2123123123123"
        return context


class contact(TemplateView):
    paginate_by = 10
    template_name = 'email.html'


class businessemailcontact(TemplateView):
    paginate_by = 10
    template_name = 'businessemail.html'


class PostDetailView(View):
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, slug):
        post = get_object_or_404(Blog, slug=slug)
        comments = post.comments.filter(active=True).order_by("-created_on")
        comment_form = CommentForm()
        header_data = NavBarHeader.objects.filter(is_active=1).order_by("row")
        dropdown_data = NavBar.objects.filter(is_active=1).order_by('position')

        context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
            'Header': header_data,  # Adding Header data to context
            'DropDown': dropdown_data  # Adding DropDown data to context
        }

        return render(request, self.template_name, context)

    def post(self, request, slug):
        post = get_object_or_404(Blog, slug=slug)
        comments = post.comments.filter(active=True).order_by("-created_on")
        new_comment = None
        header_data = NavBarHeader.objects.filter(is_active=1).order_by("row")
        dropdown_data = NavBar.objects.filter(is_active=1).order_by('position')

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = post
            new_comment.save()

        context = {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,
            'Header': header_data,  # Adding Header data to context
            'DropDown': dropdown_data  # Adding DropDown data to context
        }

        return render(request, self.template_name, context)




from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
@csrf_exempt
def subtract_currency(request):
    if request.method == 'POST':
        user = request.user
        cost = request.POST.get('cost')
        profile = ProfileDetails.objects.get(user=user)
        try:
            profile.subtract_currency(cost)
            return JsonResponse({'status': 'success'})
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Not enough currency'})


class CurrencyProductView(DetailView):
    model = CurrencyMarket
    paginate_by = 10
    template_name = "currencyproduct.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        # context['object'] = Item.objects.filter(is_active=1).order_by('slug')  #maybe change to be able to be ordered by different parameters
        # like slug, price, popularity, type (gold, platinum, emerald, diamond), etc
        # somehow limited to 3 products on first page, yet products still exist and can be accessed by "view on site"
        return context


class CurrencyMarketView(EBaseView):
    model = CurrencyMarket
    template_name = "currencymarket.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['Logos'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Favicon'] = FaviconBase.objects.filter(is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Social'] = SocialMedia.objects.filter(page=self.template_name, is_active=1)
        context['Currency'] = CurrencyMarket.objects.filter(is_active=1).order_by(
            'price')  # deals/non-deals can be seperated in the templates
        return context


class CurrencyCheckoutView(EBaseView):
    model = CheckoutBackgroundImage
    template_name = "currencycheckout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        return context

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.warning(self.request, "Please log in to see your order history.")
            return redirect("accounts/login")  # replace "login" with your login route
        try:
            order = CurrencyFullOrder.objects.get(user=self.request.user, ordered=False)
            form = CurrencyCheckoutForm()
            context = self.get_context_data()
            context['form'] = form
            context['couponform'] = CouponForm()
            context['endowmentform'] = EndowmentForm(request=self.request)
            context['order'] = order
            context['DISPLAY_COUPON_FORM'] = True
            return render(self.request, "currencycheckout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("showcase:currencycheckout")

    def post(self, *args, **kwargs):
        form = CurrencyCheckoutForm(self.request.POST or None)
        # print(self.request.GET)
        try:
            order = CurrencyFullOrder.objects.get(user=self.request.user, ordered=False)

            if form.is_valid():
                payment_option = form.cleaned_data.get('payment_option')

                if payment_option == 'S':
                    return redirect('showcase:currencypayment',
                                    payment_option='stripe')
                elif payment_option == 'P':
                    return redirect('showcase:currencypayment',
                                    payment_option='paypal')
                else:
                    messages.warning(self.request,
                                     "Invalid payment option selected")
                    return redirect('showcase:currencycheckout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("showcase:currencymarket")


from paypalrestsdk import Payment as PayPalPayment


class CurrencyPaymentView(EBaseView):
    template_name = "currencypayment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        endowment_form = EndowmentForm(request=self.request)  # Pass the request object to the form
        context['endowmentform'] = endowment_form
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")

        return context

    def get(self, *args, **kwargs):
        # request (self) does not seem to be getting user
        order = CurrencyOrder.objects.get(user=self.request.user, ordered=False)
        if order:
            context = self.get_context_data(**kwargs)
            context['order'] = order
            context['DISPLAY_COUPON_FORM'] = False
            context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
            userprofile = User.objects.get(username=self.request.user.username)
            if hasattr(userprofile, "one_click_purchasing"):
                # userprofile is probably not linked to database
                if userprofile.one_click_purchasing:
                    # fetch the users list
                    cards = stripe.Customer.list_sources(
                        userprofile.stripe_customer_id,
                        limit=3,
                        object='card'
                    )
                    card_list = cards['data']
                    if len(card_list) > 0:
                        # update the context with the default card
                        context.update({
                            'card': card_list[0]
                        })
            else:
                userprofile.one_click_purchasing = False
                return render(self.request, "currencypayment.html", context)
                # Check if PayPal payment method is available
            if hasattr(userprofile, 'paypal_enabled') and userprofile.paypal_enabled:
                context['PAYPAL_CLIENT_ID'] = settings.PAYPAL_CLIENT_ID

            return render(self.request, "currencypayment.html", context)
        else:
            messages.warning(
                self.request, "Please add a billing address.")
            return redirect("showcase:currencycheckout")

    def post(self, *args, **kwargs):
        order = CurrencyOrder.objects.get(user=self.request.user, ordered=False)
        form = CurrencyPaymentForm(self.request.POST)
        userprofile = User.objects.get(username=self.request.user.username)
        payment_method = self.request.POST.get('payment_method')

        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("expiry"))

            token = stripe.Token.create(
                card={
                    "number": form.cleaned_data.get("number"),
                    "exp_month": form.cleaned_data.get("exp_month"),
                    "exp_year": form.cleaned_data.get("exp_year"),
                    "cvc": form.cleaned_data.get("cvc"),
                },
            )
            save = form.cleaned_data.get('save')
            use_default = form.cleaned_data.get('use_default')
            user_profile = get_object_or_404(UserProfile, user=self.request.user)

            # Now you can access stripe_customer_id
            stripe_customer_id = user_profile.stripe_customer_id

            if save:
                if userprofile.stripe_customer_id != '' and userprofile.stripe_customer_id is not None:
                    customer = stripe.Customer.retrieve(userprofile.stripe_customer_id)
                    customer.sources.create(source=token)
                else:
                    customer = stripe.Customer.create(email=self.request.user.email)
                    customer.sources.create(source=token)
                    userprofile.stripe_customer_id = customer['id']
                    userprofile.one_click_purchasing = True
                    userprofile.save()

            amount = int(order.get_total_price() * 100)

            try:
                if use_default or save:
                    # charge the customer because we cannot charge the token more than once
                    charge = stripe.Charge.create(
                        amount=amount,  # cents
                        currency="usd",
                        customer=userprofile.stripe_customer_id
                    )

                    with transaction.atomic():
                        print('currency updates activated')
                        user_profile = UserProfile.objects.get(user=self.request.user)
                        currencymarket = order.items.first().items  # Assuming single item
                        user_profile.currency = currencymarket.currency
                        user_profile.currency_amount += currencymarket.amount
                        print('the currency amount is ' + currencymarket.amount)
                        user_profile.save()
                    print('the payment went through')
                else:
                    # charge once off on the token
                    charge = stripe.Charge.create(
                        amount=amount,  # cents
                        currency="usd",
                        source=token
                    )

                    def is_numeric(value):
                        """
                        Checks if a given value is a numeric type.

                        Args:
                            value: The value to check.

                        Returns:
                            True if the value is numeric, False otherwise.
                        """
                        return isinstance(value, (int, float, complex))

                    with transaction.atomic():
                        print('currency updates activated')
                        user_profile = UserProfile.objects.get(user=self.request.user)
                        print('II')
                        order = CurrencyOrder.objects.first()  # Get the first CurrencyOrder instance

                        # Access the related CurrencyMarket object
                        currencymarket = order.items

                        # Check if both variables are numeric before addition
                        if is_numeric(user_profile.currency_amount) and is_numeric(currencymarket.amount):
                            user_profile.currency = currencymarket.currency
                            print('IV')
                            user_profile.currency_amount += currencymarket.amount
                            print('the currency amount is ' + str(currencymarket.amount))
                            user_profile.save()
                        else:
                            print('Error: One or both variables are not numeric.')
                    print('the payment went through')

                # create the payment
                payment = Payment()
                payment.stripe_charge_id = charge['id']
                payment.user = self.request.user
                payment.amount = order.get_total_price()
                payment.save()
                print('your payment has been saved')

                # Access the single related item directly:
                currency_market = order.items

                # Update the order items, assuming you need to update the single related item:
                currency_market.ordered = True
                currency_market.save()  # Save the changes to the single item

                # Print update confirmation:
                print('Your payment has been updated for the ' + currency_market.name + ' item.')

                # Cart removal logic
                order_items = CurrencyOrder.objects.filter(user=self.request.user, ordered=False)
                for order_item in order_items:
                    order_item.delete()

                # Inform the user about cart clearance
                messages.success(request, "Your order has been placed! Your cart has been cleared.")

                order.ordered = True
                order.payment = payment
                order.ref_code = create_ref_code()
                print('the value of order is ' + order.ref_code)
                order.save()
                messages.success(self.request, "Your order was successful!")

                if payment_method == 'paypal':
                    return HttpResponseRedirect(self.process_paypal_payment(order))
                return redirect("showcase:currencymarket")

            except stripe.error.CardError as e:
                body = e.json_body
                err = body.get('error', {})
                messages.warning(self.request, f"{err.get('message')}")
                return redirect("showcase:currencymarket")

            except stripe.error.RateLimitError as e:
                # Too many requests made to the API too quickly
                messages.warning(self.request, "Rate limit error")
                return redirect("showcase:currencymarket")

            except stripe.error.InvalidRequestError as e:
                # Invalid parameters were supplied to Stripe's API
                print(e)
                print(12345)
                # print ('stripeToken', stripeToken)
                messages.warning(self.request, "Invalid parameters")
                return redirect("/currencymarket")

            except stripe.error.AuthenticationError as e:
                # Authentication with Stripe's API failed
                # (maybe you changed API keys recently)
                messages.warning(self.request, "Not authenticated")
                return redirect("/")

            except stripe.error.APIConnectionError as e:
                # Network communication with Stripe failed
                messages.warning(self.request, "Network error")
                return redirect("/currencymarket")

            except stripe.error.StripeError as e:
                # Display a very generic error to the user, and maybe send
                # yourself an email
                messages.warning(
                    self.request, "Something went wrong. You were not charged. Please try again."
                )
                return redirect("/currencymarket")

            except Exception as e:
                # send an email to ourselves
                messages.warning(
                    self.request, "Your order was placed!"
                )
                return redirect("/currencymarket")

        messages.warning(self.request, "Invalid data received")
        return redirect("/currencypayment/stripe")


class CurrencyPayPalExecuteView(View):
    def get(self, request, *args, **kwargs):
        payer_id = request.GET.get('PayerID')
        payment_id = request.GET.get('paymentId')

        try:
            order = CurrencyOrder.objects.get(paypal_payment_id=payment_id, ordered=False)
            paypal_payment = PayPalPayment.find(payment_id)

            if paypal_payment.execute({'payer_id': payer_id}):
                # Payment successful
                payment = Payment()
                payment.paypal_payment_id = payment_id
                payment.user = self.request.user
                payment.amount = order.get_total_price()
                payment.save()
                print('your payment has been saved')

                # Mark order items as ordered
                order_items = order.items.all()
                order_items.update(ordered=True)
                print('your payment has been updated')

                # Associate the payment with the order
                order.ordered = True
                order.payment = payment
                order.ref_code = create_ref_code()
                print('the value of order is ' + order.ref_code)
                order.save()

                messages.success(self.request, 'Your order was successful!')
                return redirect('showcase:currencymarket')

            # Payment failed
            messages.error(self.request, 'Failed to process PayPal payment')
            return redirect('/currencypayment')

        except CurrencyOrder.DoesNotExist:
            messages.error(self.request, 'Order not found')
            return redirect('/currencypayment')


class CurrencyPaypalFormView(FormView):
    template_name = 'paypalpayment.html'
    form_class = CurrencyPaypalPaymentForm

    def get_initial(self):
        return {
            'business': 'your-paypal-business-address@example.com',
            'amount': 20,
            'currency_code': 'EUR',
            'item_name': 'Example item',
            'invoice': 1234,
            'notify_url': self.request.build_absolute_uri(reverse('paypal-ipn')),
            'return_url': self.request.build_absolute_uri(reverse('paypal-return')),
            'cancel_return': self.request.build_absolute_uri(reverse('paypal-cancel')),
            'lc': 'EN',
            'no_shipping': '1',
        }


@allow_guest_user
def currency_add_to_cart(request, slug):
    item = get_object_or_404(CurrencyMarket, slug=slug)
    order_item, created = CurrencyOrder.objects.get_or_create(
        items=item,
        user=request.user,
        ordered=False,
    )

    order_qs = CurrencyFullOrder.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        # CORRECTION: Check for existing item using the appropriate field
        if any(order_item.slug == item.slug for order_item in order.items.all()):
            order_item.quantity += 1  # Assuming quantity is directly on CurrencyOrder
            order_item.save()
            messages.info(
                request,
                f"\"{order_item.item.title}\" was added to your cart."
            )
            return redirect("showcase:currencycheckout")
        else:
            order.items.add(order_item)
            messages.info(request, "The currency was added to your cart.")
            return redirect("showcase:currencycheckout")
    else:
        order_qs = CurrencyFullOrder.objects.create(
            user=request.user,
            ordered=False,
            ordered_date=timezone.now()
        )
        print("Order created")

        # CORRECTION: Same check as above
        if any(order_item.slug == item.slug for order_item in order_qs.items.all()):
            order_item.quantity += 1
            order_item.save()
            messages.info(
                request,
                f"\"{order_item.item.title}\" was added to your cart."
            )
            return redirect("showcase:currencycheckout")
        else:
            order_qs.items.add(order_item)
            messages.info(request, "You now have the currency in your cart.")
            return redirect("showcase:currencycheckout")


@login_required
def currency_remove_from_cart(request, slug):
    item = get_object_or_404(CurrencyOrder, slug=slug)
    order_qs = CurrencyFullOrder.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = CurrencyOrder.objects.filter(item=item,
                                                      user=request.user,
                                                      ordered=False)[0]
            order_item.delete()
            messages.info(
                request, "Item \"" + order_item.item.title +
                         "\" was removed from your cart")
            return redirect("showcase:currencymarket")
        else:
            messages.info(request, "This item is no longer in your cart")
            return redirect("showcase:product", slug=slug)
    else:
        # add message doesnt have order
        messages.info(request, "You do not seem to have an order currently")
        return redirect("showcase:product", slug=slug)


def currency_get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(
            request,
            "Sorry, this coupon seems to have either expired or does not exist. Do you want to try another one?"
        )
        return redirect("showcase:checkout")


class CurrencyAddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(user=self.request.user,
                                          ordered=False)
                order.coupon = get_coupon(self.request, code)
                order.save()
                messages.success(self.request, "Successfully added coupon")
                return redirect("showcase:currencycheckout")
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")
                return redirect("showcase:currencycheckout")


def index(request):
    return redirect('showcase')


@login_required
def currency_reduce_quantity_item(request, slug):
    item = get_object_or_404(CurrencyOrder, slug=slug)
    order_qs = CurrencyOrder.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = CurrencyOrder.objects.filter(item=item,
                                                      user=request.user,
                                                      ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, "Item quantity was updated")
            return redirect("showcase:order-summary")
        else:
            messages.info(request, "This Item is not in your cart")
            return redirect("showcase:order-summary")
    else:
        # add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("showcase:order-summary")


# users/views.py

# ...

# @login_required
# def profile(request, username):
#    user = get_object_or_404(User, username=username)
#    profile = get_object_or_404(Profile, user=user)
#    return render(request, 'like.html', {'profile': profile, 'user': user})

# ...

# @login_required
# def edit_profile(request):
# if request.method == "POST":
# form = EditProfileForm(request.POST, request.FILES)
# if form.is_valid():
# about_me = form.cleaned_data["about_me"]
# username = form.cleaned_data["username"]
# image = form.cleaned_data["image"]

# user = User.objects.get(id=request.user.id)
# profile = Profile.objects.get(user=user)
# user.username = username
# user.save()
# profile.about_me = about_me
# if image:
# profile.image = image
# profile.save()
# return redirect('like', username=user.username)
# else:
# form = EditProfileForm()
# return render(request, 'edit_profile.html', {'form': form})

# @login_required
# def backgroundimages(request):
#  if(request.method == "POST"):
#    form = BackgroundImagery(request.POST)
#    if(form.is_valid()):
#      post = form.save(commit=False)
#      post.save()
#      return redirect('showcase:index')
#  else:
#      form = PosteForm()
#      return render(request, 'index.html', {'form':form})
#      messages.error(request, 'Image submission failed to register, please try again.')
#      messages.error(request, form.errors)


import stripe

stripe.api_key = "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"

stripe.Source.create(type='ach_credit_transfer',
                     currency='usd',
                     owner={'email': 'PokeTroveCompany6@gmail.com'})


class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = "ehome.html"


class Featured(ListView):
    model = Item
    paginate_by = 10
    template_name = "featuredproducts.html"


class ProductView(DetailView):
    model = Item
    paginate_by = 10
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        # context['object'] = Item.objects.filter(is_active=1).order_by('slug')  #maybe change to be able to be ordered by different parameters
        # like slug, price, popularity, type (gold, platinum, emerald, diamond), etc
        # somehow limited to 3 products on first page, yet products still exist and can be accessed by "view on site"
        return context


class OrderSummaryView(EBaseView):
    model = OrderBackgroundImage
    template_name = "order-summary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        return context

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.warning(self.request, "Please log in to see your order history.")
            return redirect("accounts/login")  # replace "login" with your login route
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = self.get_context_data()
            context['object'] = order
            return render(self.request, 'order-summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("showcase:ehome")


class CheckoutView(EBaseView):
    model = CheckoutBackgroundImage
    template_name = "checkout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        return context

    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
            context = self.get_context_data()
            context['form'] = form
            context['couponform'] = CouponForm()
            context['order'] = order
            context['DISPLAY_COUPON_FORM'] = True

            shipping_address_qs = Address.objects.filter(
                user=self.request.user, address_type='S', default=True)
            if shipping_address_qs.exists():
                context.update(
                    {'default_shipping_address': shipping_address_qs[0]})

            billing_address_qs = Address.objects.filter(user=self.request.user,
                                                        address_type='B',
                                                        default=True)
            if billing_address_qs.exists():
                context.update(
                    {'default_billing_address': billing_address_qs[0]})
            return render(self.request, "checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("showcase:checkout")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        # print(self.request.GET)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():

                use_default_shipping = form.cleaned_data.get(
                    'use_default_shipping')
                if use_default_shipping:
                    print("Using the default shipping address")
                    address_qs = Address.objects.filter(user=self.request.user,
                                                        address_type='S',
                                                        default=True)
                    if address_qs.exists():
                        shipping_address = address_qs[0]
                        order.shipping_address = shipping_address
                        order.save()
                    else:

                        print("User is entering a new shipping address")
                        shipping_address1 = form.cleaned_data.get(
                            'shipping_address')
                        shipping_address2 = form.cleaned_data.get(
                            'shipping_address2')
                        shipping_country = form.cleaned_data.get(
                            'shipping_country')
                        shipping_zip = form.cleaned_data.get('shipping_zip')

                        messages.info(self.request,
                                      "No default shipping address available")
                        return redirect('showcase:checkout')
                else:
                    # change to allow for saved information without posting
                    print("shipping_address1")
                    shipping_address1 = form.cleaned_data.get(
                        'shipping_address')
                    shipping_address2 = form.cleaned_data.get(
                        'shipping_address2')
                    shipping_country = form.cleaned_data.get(
                        'shipping_country')
                    shipping_zip = form.cleaned_data.get('shipping_zip')

                    if is_valid_form(
                            [shipping_address1, shipping_country, shipping_zip]):
                        shipping_address = Address(
                            user=self.request.user,
                            street_address=shipping_address1,
                            apartment_address=shipping_address2,
                            country=shipping_country,
                            zip=shipping_zip,
                            address_type='S')
                        shipping_address.save()

                        order.shipping_address = shipping_address
                        order.save()

                        set_default_shipping = form.cleaned_data.get(
                            'set_default_shipping')
                        if set_default_shipping:
                            shipping_address.default = True
                            shipping_address.save()

                    else:
                        shipping_address = Address(
                            user=self.request.user,
                            street_address=shipping_address1,
                            apartment_address=shipping_address2,
                            country=shipping_country,
                            zip=shipping_zip,
                            address_type='S')
                        shipping_address.save()

                        order.shipping_address = shipping_address
                        order.save()

                        messages.info(
                            self.request,
                            "Please fill in the required shipping address fields"
                        )
                        # save = form.data.get('save')
                        # order.save()
                        return redirect('showcase:checkout')

                use_default_billing = form.cleaned_data.get(
                    'use_default_billing')
                same_billing_address = form.cleaned_data.get(
                    'same_billing_address')

                if same_billing_address:
                    billing_address = shipping_address
                    billing_address.pk = None
                    billing_address.save()
                    billing_address.address_type = 'B'
                    billing_address.save()
                    order.billing_address = billing_address
                    order.save()

                elif use_default_billing:
                    print("Using the default billing address")
                    address_qs = Address.objects.filter(user=self.request.user,
                                                        address_type='B',
                                                        default=True)
                    if address_qs.exists():
                        billing_address = address_qs[0]
                        order.billing_address = billing_address
                        order.save()
                    else:
                        messages.info(self.request,
                                      "No default billing address available")
                        return redirect('showcase:checkout')
                else:
                    print("User is entering a new billing address")
                    billing_address1 = form.cleaned_data.get('billing_address')
                    billing_address2 = form.cleaned_data.get(
                        'billing_address2')
                    billing_country = form.cleaned_data.get('billing_country')
                    billing_zip = form.cleaned_data.get('billing_zip')

                    if is_valid_form(
                            [billing_address1, billing_country, billing_zip]):
                        billing_address = Address(
                            user=self.request.user,
                            street_address=billing_address1,
                            apartment_address=billing_address2,
                            country=billing_country,
                            zip=billing_zip,
                            address_type='B')
                        billing_address.save()

                        order.billing_address = billing_address
                        order.save()

                        set_default_billing = form.cleaned_data.get(
                            'set_default_billing')
                        if set_default_billing:
                            billing_address.default = True
                            billing_address.save()

                    else:
                        messages.info(
                            self.request,
                            "Please fill in the required billing address fields"
                        )
                        return redirect('showcase:checkout')

                payment_option = form.cleaned_data.get('payment_option')

                if payment_option == 'S':
                    return redirect('showcase:payment',
                                    payment_option='stripe')
                elif payment_option == 'P':
                    return redirect('showcase:payment',
                                    payment_option='paypal')
                else:
                    messages.warning(self.request,
                                     "Invalid payment option selected")
                    return redirect('showcase:checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("showcase:order-summary")


from paypalrestsdk import Payment as PayPalPayment


class PaymentView(EBaseView):
    template_name = "payment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")

        return context

    def get(self, *args, **kwargs):
        # request (self) does not seem to be getting user
        order = Order.objects.get(user=self.request.user, ordered=False)
        if order.billing_address:
            context = self.get_context_data(**kwargs)
            context['order'] = order
            context['DISPLAY_COUPON_FORM'] = False
            context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
            userprofile = User.objects.get(username=self.request.user.username)
            if hasattr(userprofile, "one_click_purchasing"):
                # userprofile is probably not linked to database
                if userprofile.one_click_purchasing:
                    # fetch the users list
                    cards = stripe.Customer.list_sources(
                        userprofile.stripe_customer_id,
                        limit=3,
                        object='card'
                    )
                    card_list = cards['data']
                    if len(card_list) > 0:
                        # update the context with the default card
                        context.update({
                            'card': card_list[0]
                        })
            else:
                userprofile.one_click_purchasing = False
                return render(self.request, "payment.html", context)
                # Check if PayPal payment method is available
            if hasattr(userprofile, 'paypal_enabled') and userprofile.paypal_enabled:
                context['PAYPAL_CLIENT_ID'] = settings.PAYPAL_CLIENT_ID

            return render(self.request, "payment.html", context)
        else:
            messages.warning(
                self.request, "You have not added a billing address.")
            return redirect("showcase:checkout")

    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        form = PaymentForm(self.request.POST)
        userprofile = User.objects.get(username=self.request.user.username)
        payment_method = self.request.POST.get('payment_method')

        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("expiry"))

            token = stripe.Token.create(
                card={
                    "number": form.cleaned_data.get("number"),
                    "exp_month": form.cleaned_data.get("exp_month"),
                    "exp_year": form.cleaned_data.get("exp_year"),
                    "cvc": form.cleaned_data.get("cvc"),
                },
            )
            save = form.cleaned_data.get('save')
            use_default = form.cleaned_data.get('use_default')

            if save:
                if userprofile.stripe_customer_id != '' and userprofile.stripe_customer_id is not None:
                    customer = stripe.Customer.retrieve(userprofile.stripe_customer_id)
                    customer.sources.create(source=token)
                else:
                    customer = stripe.Customer.create(email=self.request.user.email)
                    customer.sources.create(source=token)
                    userprofile.stripe_customer_id = customer['id']
                    userprofile.one_click_purchasing = True
                    userprofile.save()

            amount = int(order.get_total_price() * 100)

            try:
                if use_default or save:
                    # charge the customer because we cannot charge the token more than once
                    charge = stripe.Charge.create(
                        amount=amount,  # cents
                        currency="usd",
                        customer=userprofile.stripe_customer_id
                    )
                    print('the payment went through')
                else:
                    # charge once off on the token
                    charge = stripe.Charge.create(
                        amount=amount,  # cents
                        currency="usd",
                        source=token
                    )
                    print('the payment went through')

                # create the payment
                payment = Payment()
                payment.stripe_charge_id = charge['id']
                payment.user = self.request.user
                payment.amount = order.get_total_price()
                payment.save()

                # assign the payment to the order
                order_items = order.items.all()
                order_items.update(ordered=True)
                print('your order payment has been updated')
                for item in order_items:
                    item.save()

                order.ordered = True
                order.payment = payment
                order.ref_code = create_ref_code()
                order.save()

                messages.success(self.request, "Your order was successful!")

                if payment_method == 'paypal':
                    return HttpResponseRedirect(self.process_paypal_payment(order))
                return redirect("showcase:ehome")

            except stripe.error.CardError as e:
                body = e.json_body
                err = body.get('error', {})
                messages.warning(self.request, f"{err.get('message')}")
                return redirect("showcase:ehome")

            except stripe.error.RateLimitError as e:
                # Too many requests made to the API too quickly
                messages.warning(self.request, "Rate limit error")
                return redirect("showcase:ehome")

            except stripe.error.InvalidRequestError as e:
                # Invalid parameters were supplied to Stripe's API
                print(e)
                print(12345)
                # print ('stripeToken', stripeToken)
                messages.warning(self.request, "Invalid parameters")
                return redirect("/ehome")

            except stripe.error.AuthenticationError as e:
                # Authentication with Stripe's API failed
                # (maybe you changed API keys recently)
                messages.warning(self.request, "Not authenticated")
                return redirect("/")

            except stripe.error.APIConnectionError as e:
                # Network communication with Stripe failed
                messages.warning(self.request, "Network error")
                return redirect("/ehome")

            except stripe.error.StripeError as e:
                # Display a very generic error to the user, and maybe send
                # yourself an email
                messages.warning(
                    self.request, "Something went wrong. You were not charged. Please try again."
                )
                return redirect("/ehome")

            except Exception as e:
                # send an email to ourselves
                messages.warning(
                    self.request, "A serious error occurred. We have been notified."
                )
                return redirect("/ehome")

        messages.warning(self.request, "Invalid data received")
        return redirect("/payment/stripe")


class PayPalExecuteView(View):
    def get(self, request, *args, **kwargs):
        payer_id = request.GET.get('PayerID')
        payment_id = request.GET.get('paymentId')

        try:
            order = Order.objects.get(paypal_payment_id=payment_id, ordered=False)
            paypal_payment = PayPalPayment.find(payment_id)

            if paypal_payment.execute({'payer_id': payer_id}):
                # Payment successful
                payment = Payment()
                payment.paypal_payment_id = payment_id
                payment.user = self.request.user
                payment.amount = order.get_total_price()
                payment.save()

                # Mark order items as ordered
                order_items = order.items.all()
                order_items.update(ordered=True)

                # Associate the payment with the order
                order.ordered = True
                order.payment = payment
                order.ref_code = create_ref_code()
                order.save()

                messages.success(self.request, 'Your order was successful!')
                return redirect('showcase:ehome')

            # Payment failed
            messages.error(self.request, 'Failed to process PayPal payment')
            return redirect('/payment')

        except Order.DoesNotExist:
            messages.error(self.request, 'Order not found')
            return redirect('/payment')


class PaypalFormView(FormView):
    template_name = 'paypalpayment.html'
    form_class = PaypalPaymentForm

    def get_initial(self):
        return {
            'business': 'your-paypal-business-address@example.com',
            'amount': 20,
            'currency_code': 'EUR',
            'item_name': 'Example item',
            'invoice': 1234,
            'notify_url': self.request.build_absolute_uri(reverse('paypal-ipn')),
            'return_url': self.request.build_absolute_uri(reverse('paypal-return')),
            'cancel_return': self.request.build_absolute_uri(reverse('paypal-cancel')),
            'lc': 'EN',
            'no_shipping': '1',
        }


@allow_guest_user
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False,
        # id=10,
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(
                request,
                "\"" + order_item.item.title + "\" was added to your cart.")
            return redirect("showcase:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("showcase:order-summary")
    else:
        order_qs = Order.objects.create(user=request.user,
                                        ordered=False,
                                        ordered_date=timezone.now())
        print("Order created")
        # check if the order item is in the order
        if order_qs.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(
                request,
                "\"" + order_item.item.title + "\" was added to your cart.")
            return redirect("showcase:order-summary")
        else:
            order_qs.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("showcase:order-summary")


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item,
                                                  user=request.user,
                                                  ordered=False)[0]
            order_item.delete()
            messages.info(
                request, "Item \"" + order_item.item.title +
                         "\" was removed from your cart")
            return redirect("showcase:order-summary")
        else:
            messages.info(request, "This item is no longer in your cart")
            return redirect("showcase:product", slug=slug)
    else:
        # add message doesnt have order
        messages.info(request, "You do not seem to have an order currently")
        return redirect("showcase:product", slug=slug)


def index(request):
    return redirect('showcase')


@login_required
def reduce_quantity_item(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item,
                                                  user=request.user,
                                                  ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, "Item quantity was updated")
            return redirect("showcase:order-summary")
        else:
            messages.info(request, "This Item is not in your cart")
            return redirect("showcase:order-summary")
    else:
        # add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("showcase:order-summary")


import random
import string

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CouponForm, RefundForm, PaymentForm


# from .models import Address, Coupon, Refund, UserProfile

# stripe.api_key = settings.STRIPE_SECRET_KEY


def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits,
                                  k=20))


from django.db.models import Count, Avg


def products(request):
    context = {'items': Item.objects.all()}
    return render(request, "products.html", context)


def reviewproducts(request, pid):
    product = Item.objects.get(pid=pid)

    products = ProductReview.objects.filter(product=product).order_by("-date")

    # getting the reviews
    reviews = ProductReview.objects.filter(Item=Item)

    average_rating = ProductReview.objects.filter(Item=Item).aggregate(rating=Avg('rating'))

    p_image = Item.image.all()

    context = {
        "p": products,
        "p_image": p_image,
        "average_rating": average_rating,
        "review": review,
        "products": products,
    }

    return render(request, "showcase:index.html", context)


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


class ItemDetailView(DetailView):
    model = Item
    paginate_by = 10
    template_name = "product.html"


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item,
                                                  user=request.user,
                                                  ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("showcase:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("showcase:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("showcase:product", slug=slug)


def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(
            request,
            "Sorry, this coupon seems to have either expired or does not exist. Do you want to try another one?"
        )
        return redirect("showcase:checkout")


class AddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(user=self.request.user,
                                          ordered=False)
                order.coupon = get_coupon(self.request, code)
                order.save()
                messages.success(self.request, "Successfully added coupon")
                return redirect("showcase:checkout")
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")
                return redirect("showcase:checkout")


class RequestRefundView(View):
    def get(self, *args, **kwargs):
        form = RefundForm()
        context = {'form': form}
        return render(self.request, "request_refund.html", context)

    def post(self, *args, **kwargs):
        form = RefundForm(self.request.POST)
        if form.is_valid():
            ref_code = form.cleaned_data.get('ref_code')
            message = form.cleaned_data.get('message')
            email = form.cleaned_data.get('email')
            # edit the order
            try:
                order = Order.objects.get(ref_code=ref_code)
                order.refund_requested = True
                order.save()

                # store the refund
                refund = Refund()
                refund.order = order
                refund.reason = message
                refund.email = email
                refund.save()

                messages.info(self.request, "Your request was received.")
                return redirect("showcase:request-refund")

            except ObjectDoesNotExist:
                messages.info(self.request, "This order does not exist.")
                return redirect("showcase:request-refund")


from django.contrib.auth.forms import UserChangeForm


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'showcase/profile.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.CreateView):
    form_class = UserChangeForm
    template_name = 'showcase:edit_profile.html'
    success_url = reverse_lazy('login')


# from .models import PublicProfile
# from .forms import PublicForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

# def edit_user(request, pk):
# querying the User object with pk from url
# user = User.objects.get(pk=pk)

# prepopulate UserProfileForm with retrieved user values from above.
# user_form = PublicForm(instance=user)

# The sorcery begins from here, see explanation below
# ProfileInlineFormset = inlineformset_factory(User, PublicProfile, fields=('website', 'bio', 'phone', 'city', 'country', 'organization'))
# formset = ProfileInlineFormset(instance=user)

# if request.user.is_authenticated() and request.user.id == user.id:
# if request.method == "POST":
# user_form = PublicForm(request.POST, request.FILES, instance=user)
# formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

# if user_form.is_valid():
# created_user = user_form.save(commit=False)
# formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

# if formset.is_valid():
# created_user.save()
# formset.save()
# return HttpResponseRedirect('/accounts/profile/')

# return render(request, "account/account_update.html", {
# "noodle": pk,
# "noodle_form": user_form,
# "formset": formset,
# })
# else:
# raise PermissionDenied

# from .forms import NewUserForm, UserForm, ProfileForm

# def userpage(request):
# if request.method == "POST":
# user_form = UserForm(request.POST, instance=request.user)
# profile_form = ProfileForm(request.POST, instance=request.user.profile)
# if user_form.is_valid():
# user_form.save()
# messages.success(request,('Your profile was successfully updated!'))
# elif profile_form.is_valid():
#    profile_form.save()
#    messages.success(request,('Your wishlist was successfully updated!'))
# else:
#    messages.error(request,('Unable to complete request'))
# return redirect ("showcase:userpage")
# user_form = UserForm(instance=request.user)
# profile_form = ProfileForm(instance=request.user.profile)
# return render(request = request, template_name ="showcase/user.html", context = {"user":request.user,
#  "user_form": user_form, "profile_form": profile_form })

# @def products(request):
#  if request.method == "POST":
#     product_id = request.POST.get("product_pk")
#     product = Product.objects.get(id = product_id)
#     request.user.profiletwo.products.add(product)
#     messages.success(request,(f'{product} added to wishlist.'))
#     return redirect ('showcase:products')
#  products = Product.objects.all()
#  paginator = Paginator(products, 18)
#  page_number = request.GET.get('page')
#  page_obj = paginator.get_page(page_number)
#  return render(request = request, template_name="showcase/products.html", context = { "page_obj":page_obj})

# from .models import ExtendUser
# Create your views here.

# def phome(request):
#    data = request.user
#    return render(request,'showcase/profile.html',{'data':data})

from .forms import (EditProfileForm)

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# from django.contrib.auth.decorators import login_required

# def index1(request):
# return HttpResponse('Welcome to my Registration System')
#    numbers = [1,2,3,4,5]
#    name = 'apoorva'

#    args ={'myname':name, 'mynums':numbers}
#    return render(request,'showcase/index.html',args)


def profile(request, user):
    args = {'user': user}
    return render(request, 'profile.html', args)


# views.py
def edit_profile(request, pk):
    # Your view logic here
    # The 'pk' parameter will now be passed from the URL

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('showcase:profile', pk=pk)

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileDetail
from .models import ProfileDetails


class ProfileEditView(FormView):
    template_name = 'profile_edit.html'
    form_class = ProfileDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        return context

    def form_valid(self, form):
        profile = form.save(commit=False)  # Don't save to DB yet
        profile.user = self.request.user  # Set the user
        profile.save()  # Now save to DB
        return redirect('showcase:profile', pk=profile.pk)

    def post(self, request, pk=None):
        profile = ProfileDetails.objects.filter(user=request.user).first()
        if profile:
            form = self.form_class(request.POST, request.FILES, instance=profile)
        else:
            form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)  # Don't save to DB yet
            profile.user = request.user  # Set the user
            profile.save()  # Now save to DB
            return redirect('showcase:profile', pk=profile.pk)
        return render(request, self.template_name, {'form': form})


class SignupView(FormMixin, ListView):
    model = SignupBackgroundImage
    template_name = "cv-form.html"
    form_class = SignUpForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup'] = SignupBackgroundImage.objects.all()
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Favicons'] = FaviconBase.objects.filter(is_active=1)
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        return context

    def post(self, request, *args, **kwargs):
        print('signup')
        if request.method == 'POST':
            print('post')
            form = SignUpForm(request.POST)
            if form.is_valid():
                print('is_valid')
                user = form.save()
                user.refresh_from_db()
                # load the profile instance created by the signal
                user.save()
                raw_password = form.cleaned_data.get('password')

                # login user after signing up
                user = form.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                subject = "Welcome to IntelleX!"
                message = 'Hello {user.username}, thank you for becoming a member of the IntelleX Community!'
                email_from = settings.EMAIL_HOST_USER
                recipent_list = [user.email, ]
                send_mail(subject, message, email_from, recipent_list)

                # redirect user to home page
                return redirect('showcase:showcase')
                messages.info(request, "You have signed up successfully! Welcome!")
        else:
            form = SignUpForm()
        return render(request, 'cv-form.html', {'form': form})


class ChangePasswordView(BaseView):
    model = ChangePasswordBackgroundImage
    template_name = "/accounts/change-password.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['Change'] = ChangePasswordBackgroundImage.objects.all()
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1).order_by("section")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Favicons'] = FaviconBase.objects.filter(is_active=1)
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        return context


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/login')
            # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # return HttpResponseRedirect('showcase:accounts/login')

        else:
            return redirect('showcase:accounts/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'registration/change-password.html', args)


from .forms import (
    RegistrationForm, )


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showcase/index.html')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'registration/regform.html', args)


@allow_guest_user
def my_view(request):
    assert request.user.is_authenticated
    return render(request, "showcase.html")


from django.urls import reverse

stripe.api_key = "sk_test_51JSB5LH4sbqF1dn75jWAc2wiQvhKq0HfNkQXthKPYmycweqQQkmyTSYgY0vzxQadtgDd2j1RqXYglHspHQXb22kG0086JLfOxS"

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        customer_email = session["customer_details"]["email"]
        product_id = session["metadata"]["product_id"]

        product = Product.objects.get(id=product_id)

        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. Here is the product you ordered. The URL is {product.url}",
            recipient_list=[customer_email],
            from_email="IntelleXCompany.com"
        )

        # TODO - decide whether you want to send the file or the URL

    elif event["type"] == "payment_intent.succeeded":
        intent = event['data']['object']

        stripe_customer_id = intent["customer"]
        stripe_customer = stripe.Customer.retrieve(stripe_customer_id)

        customer_email = stripe_customer['email']
        product_id = intent["metadata"]["product_id"]

        product = Product.objects.get(id=product_id)

        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. Here is the product you ordered. The URL is {product.url}",
            recipient_list=[customer_email],
            from_email="matt@test.com"
        )

    return HttpResponse(status=200)


class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        try:
            req_json = json.loads(request.body)
            customer = stripe.Customer.create(email=req_json['email'])
            product_id = self.kwargs["pk"]
            product = Product.objects.get(id=product_id)
            intent = stripe.PaymentIntent.create(
                amount=product.price,
                currency='usd',
                customer=customer['id'],
                metadata={
                    "product_id": product.id
                }
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})


class DonateView(ListView):
    model = DonorBackgroundImage
    template_name = "donate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['Change'] = ChangePasswordBackgroundImage.objects.all()
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1).order_by("section")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Favicons'] = FaviconBase.objects.filter(is_active=1)
        context['TextFielde'] = TextBase.objects.filter(is_active=1, page=self.template_name).order_by("section")
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['donation'] = Donate.objects.filter(is_active=1)
        context['Image'] = ImageBase.objects.filter(page=self.template_name, is_active=1)
        return context

    def donate(request):
        return render(request, 'donate.html')

        # Retrieve the author's profile avatar
        donors = Donate.objects.filter(is_active=1)

        context['Donator'] = donors

        for donors in context['Donator']:
            image = donors.image
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                donors.donor_profile_picture_url = profile.avatar.url
                donors.donor_profile_url = donors.get_profile_url()

        return context


def charge(request):
    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])
        nickname = request.POST.get('nickname')
        anonymous = request.POST.get('anonymous') == 'on'

        donation = Donate.objects.create(
            amount=amount,
            donor=request.user,
            nickname=nickname,
            anonymous=anonymous,  # You can set this to True if needed based on the donation form
            is_active=1,  # Set the donation as active
        )
        customer = stripe.Customer.create(email=request.POST['email'],
                                          name=request.POST['nickname'],
                                          source=request.POST['stripeToken']
                                          # stripetoken not defined
                                          )

        charge = stripe.Charge.create(customer=customer,
                                      amount=amount * 100,
                                      currency='usd',
                                      description="Donation")

    return redirect(reverse('showcase:patreoned', args=[amount]))


class PatreonedView(ListView):
    model = DonorBackgroundImage
    template_name = "patreoned.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['Change'] = ChangePasswordBackgroundImage.objects.all()
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1).order_by("section")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Favicons'] = FaviconBase.objects.filter(is_active=1)
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        return context

    def successMsg(request, args):
        amount = args
        return render(request, 'patreoned.html', {'amount': amount})


class DonateHistoryView(ListView):
    model = DonorBackgroundImage
    template_name = "mydonationhistory.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['Change'] = ChangePasswordBackgroundImage.objects.all()
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1).order_by("section")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Favicons'] = FaviconBase.objects.filter(is_active=1)
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)
        context['donations'] = Donate.objects.filter(donor=self.request.user, is_active=1)
        return context


class DonationsView(ListView):
    model = DonorBackgroundImage
    template_name = "donors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['Change'] = ChangePasswordBackgroundImage.objects.all()
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1).order_by("section")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Favicons'] = FaviconBase.objects.filter(is_active=1)
        # context['queryset'] = Blog.objects.filter(status=1).order_by('-created_on')
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1)

        # Assuming the ProfileDetails model has a ForeignKey named 'user' that links to the User model to represent the user's profile details.

        # Retrieve the author's profile avatar
        donation = Donate.objects.filter(is_active=1).order_by('-timestamp')

        context['donations'] = donation

        for donation in context['donations']:
            profile = ProfileDetails.objects.filter(user=donation.donor).first()
            if profile:
                donation.donor_profile_picture_url = profile.avatar.url
                donation.donor_profile_url = donation.get_profile_url()

        return context


from django.http import JsonResponse
from .models import UserProfile


def get_user_currency(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        currency_amount = profile.currency_amount
        currency_symbol = profile.currency.symbol  # Assuming 'Currency' has a 'symbol' field
        return JsonResponse({"currency_amount": currency_amount, "currency_symbol": currency_symbol})
    else:
        return JsonResponse({"error": "User not authenticated"}, status=403)


@allow_guest_user
def hello_guest(request):
    """
  This view will always have an authenticated user, but some may be guests.
  The default username generator will create a UUID4.

  Example response: "Hello, b5daf1dd-1a2f-4d18-a74c-f13bf2f086f7!
  """
    return HttpResponse("Hello, {request.user.username}!")


from guest_user.decorators import guest_user_required

from django.template.response import TemplateResponse


@guest_user_required
def why_convert(request):
    """Show reasons why to convert, only for guest users."""
    return TemplateResponse("reasons-to-convert.html")


from django.dispatch import receiver


class ContactViewe(CreateView):
    template_name = 'contact.html'
    form_class = ContactForme
    success_url = reverse_lazy('showcase:success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Contact'] = Contact.objects.order_by('-id').first()
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        print(context["Contact"])
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        return context

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


class ContactSuccessView(BaseView):
    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Contact'] = Contact.objects.all()[len(Contact.objects.all()) - 1]
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        print(context["Contact"])
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        return context


from twilio.rest import Client
from .forms import SellerApplicationForm

from django_otp.plugins.otp_totp.models import TOTPDevice
from .forms import SellerApplicationForm

import pyotp
import qrcode
from django.shortcuts import render
from io import BytesIO
from django.http import FileResponse

import base64
from django.core.mail import send_mail
import pyotp


class SellerApplicationView(FormMixin, LoginRequiredMixin, ListView):
    model = SellerApplication
    template_name = "sellerapplication.html"
    form_class = SellerApplicationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PostBackgroundImage'] = PostBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        return context

    # @login_required
    def post(self, request, *args, **kwargs):
        form = SellerApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            application = form.save()

            # Create a TOTP device for the user
            device = TOTPDevice.objects.create(user=application.user)
            device.save()

            # Base32-encode the binary key
            secret_key = base64.b32encode(device.bin_key).decode()

            # Generate OTP
            totp = pyotp.TOTP(secret_key)
            otp = totp.now()

            user = form.save()
            subject = "Your One-Time Password"
            message = f'Your OTP is: {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipent_list = [application.email, ]
            send_mail(subject, message, email_from, recipent_list)

            # Save device id in session for later verification
            request.session['device_id'] = device.id

            return redirect('showcase:verify_otp')
        else:
            form = SellerApplicationForm()


import base64
from django.http import HttpResponse
from PIL import Image
import io


def submit_seller_application(request):
    if request.method == 'POST':
        form = SellerApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()

            # Create a TOTP device for the user
            device = TOTPDevice.objects.create(user=application.user)
            device.save()

            # Generate a secret key for the user
            secret_key = device.bin_key

            # Generate a provision URL for the OTP, this URL contains the secret key
            otp_provision_uri = pyotp.totp.TOTP(secret_key).provisioning_uri(name=request.user.email,
                                                                             issuer_name='YourApp')

            # Generate a QR code from the provision URL
            qr_img = qrcode.make(otp_provision_uri)

            # Save the QR code to a BytesIO object
            byte_arr = io.BytesIO()
            qr_img.save(byte_arr, format='PNG')
            byte_arr.seek(0)

            # Convert the BytesIO object to a base64-encoded string
            base64_image = base64.b64encode(byte_arr.getvalue()).decode('utf-8')

            # Save device id in session for later verification
            request.session['device_id'] = device.id

            # Pass the base64-encoded string to the template
            return render(request, 'submit_application.html',
                          {'form': form, 'qr_code_data_url': f'data:image/png;base64,{base64_image}'})
    else:
        form = SellerApplicationForm()

    return render(request, 'submit_application.html', {'form': form})


def verify_otp(request):
    if request.method == 'POST':
        user_entered_otp = request.POST.get('otp')

        # Get the device id from the session
        device_id = request.session.get('device_id')

        # Get the TOTP device
        device = TOTPDevice.objects.get(id=device_id)

        # Base32-encode the binary key
        secret_key = base64.b32encode(device.bin_key).decode()

        # Generate OTP
        totp = pyotp.TOTP(secret_key)

        # Verify the OTP
        if totp.verify(int(user_entered_otp)):  # Convert user_entered_otp to int
            application = SellerApplication.objects.get(user=request.user)
            application.email_verified = True
            application.save()

            messages.success(request, 'OTP verified successfully.')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return render(request, 'verify_otp.html')

        try:
            profile = ProfileDetails.objects.get(user=request.user)
            profile.email = application.email
            profile.save()
        except ProfileDetails.DoesNotExist:
            messages.error(request, 'Profile details not found.')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')

        try:
            user = request.user
            user.email = application.email
            user.first_name = application.first_name
            user.last_name = application.last_name
            user.save()
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')

        return redirect('showcase:ehome')

    return render(request, 'verify_otp.html')


class BusinessEmailViewe(CreateView):
    template_name = 'businessemail.html'
    form_class = BusinessContactForm
    success_url = reverse_lazy('showcase:businessmailingsuccess')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


class BusinessEmailSuccessView(BaseView):
    template_name = 'businessmailingsuccess.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ProductBackgroundImage'] = ProductBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['BusinessMailingContact'] = BusinessMailingContact.objects.all()[
            len(BusinessMailingContact.objects.all()) - 1]
        print(context["BusinessMailingContact"])
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        return context


from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import FeedbackForm
import json
import datetime

from .fusioncharts import FusionCharts
from showcase.models import Feedback
from django.core.mail import send_mail

data = [
    ['Year', 'Sales', 'Expenses'],
    [2004, 1000, 400],
    [2005, 1170, 460],
    [2006, 660, 1120],
    [2007, 1030, 540]
]


def detail(request, slug):
    try:
        item = Item.objects.get(slug=slug)
    except Item.DoesNotExist:
        raise Http404("Product does not exist")
    company_list = Item.objects.all()
    context = {
        "company_list": company_list,
        "Item": Item,

    }
    return render(request, 'review_detail.html', context)


def review(request, slug):
    if request.POST:
        form = FeedbackForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/thanks')
    else:
        form = FeedbackForm()

    try:
        company = Item.objects.get(Item, slug=slug)
    except Item.DoesNotExist:
        raise Http404("Product does not exist")
    context = {
        "Item": Item,
        "form": form,

    }
    return render(request, 'reviews.html', context)


def index(request):
    username = request.user.username
    is_employee = request.user.groups.filter(name='Employees').exists()
    is_manager = request.user.groups.filter(name='Managers').exists()

    if is_employee:
        company_list = Item.objects.filter(employee=request.user)
        context = {
            "companies": company_list,
            "is_employee": is_employee,
            "is_manager": is_manager
        }

        return render(request, 'employee_index.html', context)
    elif request.user.is_staff:

        dataSource = {}
        # setting chart cosmetics
        dataSource['chart'] = {
            "caption": "Graph for Companies versus their respective reviews",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "xaxisname": "Companies",
            "yaxisname": "Reviews",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor": "#999999",
            "showValues": "0",
            "divlineColor": "#999999",
            "divLineIsDashed": "1",
            "showAlternateHGridColor": "0",
            "exportEnabled": "1"
        }

        reviewsDataSource = {}
        # setting chart cosmetics
        reviewsDataSource['chart'] = {
            "caption": "Number of reviews added",
            "subcaption": "Last Year",
            "borderAlpha": "20",
            "canvasBorderAlpha": "0",
            "usePlotGradientColor": "0",
            "xaxisname": "Months",
            "yaxisname": "Reviews",
            "plotBorderAlpha": "10",
            "showXAxisLine": "1",
            "xAxisLineColor": "#999999",
            "showValues": "0",
            "divlineColor": "#999999",
            "divLineIsDashed": "1",
            "showAlternateHGridColor": "0",
            "exportEnabled": "1"
        }

        reviewsDataSource['data'] = []

        for i in range(1, 13):
            data = {}
            currentMonth = datetime.date(2008, i, 1).strftime('%B')
            data['label'] = currentMonth
            count = 0
            for key in Feedback.objects.all():
                if currentMonth == key.timestamp.strftime("%B"):
                    count = count + 1
            data['value'] = count
            reviewsDataSource['data'].append(data)

        dataSource['data'] = []
        # The data for the chart should be in an array wherein each element of the array is a JSON object as
        # `label` and `value` keys.
        # Iterate through the data in `Country` model and insert in to the `dataSource['data']` list.
        for key in Company.objects.all():
            data = {}
            data['label'] = key.name
            data['value'] = Feedback.objects.filter(Company=key).count()
            dataSource['data'].append(data)

        column2D = FusionCharts("column2D", "ex1", "600", "400", "chart-1", "json", dataSource)

        column3D = FusionCharts("column2D", "ex2", "600", "400", "chart-2", "json", reviewsDataSource)

        company_list = Company.objects.all()
        review_list = Feedback.objects.all()
        employees = User.objects.filter(groups__name='Employees')
        managers = User.objects.filter(groups__name='Managers')

        context = {
            "companies": company_list,
            "employees": employees,
            "managers": managers,
            "chart": column2D.render(),
            "chart2": column3D.render(),
            "reviews": review_list,
            "latestReviews": Feedback.objects.order_by('-timestamp')[:5]
        }

        return render(request, 'admin_index.html', context)
    elif is_manager:
        employees = User.objects.filter(groups__name='Employees')
        companies = Company.objects.all()

        context = {
            "employees": employees,
            "companies": companies
        }

        return render(request, 'manager_index.html', context)
    else:
        companies = Company.objects.all()

        context = {
            "companies": companies,
        }

        return render(request, 'customer_index.html', context)


def thanks(request):
    return render(request, 'thank-you.html')


"""@login_required(login_url='/accounts/login/')
def create_company(request):
   if request.POST:
       form = CompanyForm(request.POST)

       if form.is_valid():
           instance = form.save(commit=False)
           instance.save()
           return HttpResponseRedirect('/thanks')
   else:
       form = CompanyForm()
   return render(request,'create_company.html',{'form':form })"""

from django.template.loader import render_to_string


def sendEmployeeEmailOnAddReview(Company, form):
    subject, from_email, to = "Tech Greatness.com : A customer has added a review", "IntelleXCompany1@gmail.com", \
        Company.employee.email

    context = {
        "employee": Company.employee.get_full_name(),
        "Company": Company,
        "form": form,
        "first_name": form.cleaned_data['first_name'],
        "last_name": form.cleaned_data['last_name'],
        "comment": form.cleaned_data['comment'],
    }

    msg_plain = render_to_string('add_review_email_template.txt', context)
    msg_html = render_to_string('add_review_email_template.html', context)

    send_mail(subject, msg_plain, from_email, [to], fail_silently=False, html_message=msg_html)


from .models import Item


@login_required
def my_orders(request):
    # Retrieve orders for the current logged-in user
    orders = Order.objects.filter(user=request.user)
    return render(request, 'my_orders.html', {'orders': orders})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Order, Feedback
from .forms import FeedbackForm


@login_required
def create_feedback(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.order = order
            feedback.save()
            return redirect('my_orders')
    else:
        form = FeedbackForm()
    return render(request, 'create_feedback.html', {'form': form})


from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Feedback  # Import your Feedback model here


class FeedbackView(BaseView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'review_detail.html'
    context_object_name = 'feedback'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['SettingsModel'] = SettingsModel.objects.filter(is_active=1)
        context['Items'] = Item.objects.filter(is_active=1)
        context['Image'] = ImageBase.objects.filter(is_active=1, page=self.template_name)
        # Retrieve the author's profile avatar

        slug = self.kwargs.get('slug')

        # Check if a valid slug is provided
        if slug:
            # Retrieve all feedback objects with the same slug
            feedback_objects = Feedback.objects.filter(slug=slug)

            # Add the feedback_objects to the context
            context['Feed'] = feedback_objects

        for feedback_objects in context['Feed']:
            user = feedback_objects.username
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                feedback_objects.newprofile_profile_picture_url = profile.avatar.url
                feedback_objects.newprofile_profile_url = feedback_objects.get_profile_url2()

        return context


"""@method_decorator(login_required, name='dispatch')
class FeedbackView(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    paginate_by = 10
    template_name = 'review_detail.html'
    context_object_name = 'feedback'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['SettingsModel'] = SettingsModel.objects.filter(is_active=1)
        context['Items'] = Item.objects.filter(is_active=1)

        # Get the slug from the URL
        slug = self.kwargs.get('slug')

        # Check if a valid slug is provided
        if slug:
            # Retrieve all feedback objects with the same slug
            feedback_objects = Feedback.objects.filter(slug=slug)

            # Add the feedback_objects to the context
            context['feedback_objects'] = feedback_objects

        user = self.request.user
        if user.is_authenticated:
            context['Profile'] = ProfileDetails.objects.filter(is_active=1, user=user)
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                context['profile_pk'] = profile.pk
                context['profile_url'] = reverse('showcase:profile', kwargs={'pk': profile.pk})

        # settings to alter the username & password
        # Dynamically generate the success URL
        context['success_url'] = reverse('feedbackfinish')

        return context

"""

"""
class FeedbackView(LoginRequiredMixin, FormView):
    model = FeedbackBackgroundImage
    template_name = "review_detail.html"
    form_class = FeedbackForm
    success_url = '/feedbackfinish'

    def get_context_data(self, **kwargs):
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
            context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
            context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
            context['Feed'] = Feedback.objects.filter(is_active=1).order_by("slug")
            context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
            context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
            context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")

            # Retrieve the item
            product = Item.objects.filter(is_active=1)

            context['Products'] = product

            for product in context['Products']:
                image = product.image
                item = Item.objects.filter(slug=product.slug).first()
                if product:
                    product.title = item.title
                    product.price = item.price
                    product.discount_price = item.discount_price
                    product.image_url = item.image.url
                    product.hyperlink = item.get_profile_url()

            return context

    def form_valid(self, form):
        # Save the feedback instance
        feedback = form.save(commit=False)
        feedback.username = self.request.user.username  # Set the username to the current user
        feedback.save()
        messages.success(self.request, 'Your feedback has been submitted successfully.')
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        cleaned_data = self.form.cleaned_data

        # Process the data (assuming Feedback is your model)
        feedback = Feedback()
        feedback.item = cleaned_data['item']
        feedback.order = cleaned_data['order']
        feedback.username = cleaned_data['username']
        feedback.comment = cleaned_data['comment']
        feedback.feedbackpage = cleaned_data['feedbackpage']
        feedback.slug = cleaned_data['slug']
        feedback.star_rating = cleaned_data['star_rating']
        feedback.showcase = cleaned_data['showcase']
        feedback.image = cleaned_data['image']
        feedback.image_length = cleaned_data['image_length']
        feedback.feedbackpage = cleaned_data['feedbackpage']
        feedback.image_width = cleaned_data['image_width']
        feedback.timestamp = cleaned_data['timestamp']
        feedback.is_active = cleaned_data['is_active']
        # ...

        feedback.save()

        messages.success(request, 'Your feedback has been submitted successfully.')
        return redirect('showcase:feedbackfinish')"""


class ReviewView(BaseView):
    model = ShowcaseBackgroundImage
    template_name = "reviews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['ShowcaseBackgroundImage'] = ShowcaseBackgroundImage.objects.all()
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['Titles'] = Titled.objects.filter(is_active=1).order_by("page")
        # context['Feed'] = Feedback.objects.filter(is_active=1).order_by("slug")
        # Retrieve the item

        product = Item.objects.filter(is_active=1)

        context['Products'] = product

        for product in context['Products']:
            image = product.image
            item = Item.objects.filter(slug=product.slug).first()
            if product:
                product.title = item.title
                product.price = item.price
                product.discount_price = item.discount_price
                product.image_url = item.image.url
                product.hyperlink = item.get_profile_url()

        feeder = Feedback.objects.filter(is_active=1).order_by('-timestamp')

        context['FeedBacking'] = feeder

        for feeder in context['FeedBacking']:
            user = feeder.username
            profile = ProfileDetails.objects.filter(user=user).first()
            if profile:
                feeder.user_profile_picture_url = profile.avatar.url
                feeder.user_profile_url = feeder.get_profile_url()

                print('imgsrcimg')

        return context


"""
   def form_valid(self, form):
       # Save the feedback instance
       feedback = form.save(commit=False)
       feedback.username = self.request.user.username  # Set the username to the current user
       feedback.save()
       form = FeedbackForm(request=request)
       messages.success(self.request, 'Your feedback has been submitted successfully.')
       return super().form_valid(form)

   def get_queryset(self):
       queryset = super().get_queryset()
       if self.request.user.is_authenticated:
           # Filter feedback objects based on the current user's orders
           queryset = queryset.filter(order__user=self.request.user)
       else:
           # If user is not authenticated, return an empty queryset
           queryset = Feedback.objects.none()
       return queryset

   def test_func(self):
       feedback = self.get_object()
       order = feedback.OrderItem
       return self.request.user == OrderItem.user

   def post(self, request, *args, **kwargs):
       # Process the submitted feedback form data
       feedback = self.get_object()
       order = feedback.OrderItem
       if self.request.user == OrderItem.user:
           # Process the submitted feedback form data
           # ...

           messages.success(request, 'Your feedback has been submitted successfully.')
           return redirect('showcase:feedbackfinish')
       else:
           messages.error(request, 'You are not allowed to submit feedback for this order.')
           return redirect('showcase:ehome')

   @login_required
   def get_current_user(self, request, feedback):
       if request.method == 'POST':
           # Process the form submission
           username = request.user.username
           post = form.save(commit=False)
           post.save()
           # redirect user to staffdone
           return redirect('showcase:feedbackfinish')


   def getobject(self, request, item):
       item = Item.objects.get(pk=item)

       return render(request, 'review_detail.html', {'item': item})

   def create_review(request, orderitem_id):
       try:
           Item = Item.objects.get(slug=slug)
       except Item.DoesNotExist:
           raise Http404("Product does not exist")
       if request.POST:
           form = FeedbackForm(request.POST)
           url = '/'
           data = json.dumps(url)

           if form.is_valid():
               instance = form.save(commit=False)
               instance.Item = item
               instance.save()
               sendEmployeeEmailOnAddReview(Item, form)
               return HttpResponse(data, content_type='application/json')
       else:
           form = FeedbackForm()
       context = {
           "Item": Item,
           "form": form,

       }
       return render(request, 'create_review.html', context)
"""


@login_required
def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Blog, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.blog = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request, template_name, {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form
        })


@login_required
def postpreference(request, post_name, like_or_dislike):
    if request.method == "POST":
        eachpost = get_object_or_404(Blog, slug=post_name)

        if int(like_or_dislike) == 1:
            # If the user has already liked this post, remove the like.
            if request.user in eachpost.likes.iterator():
                eachpost.likes.remove(request.user)
            else:
                # Otherwise, add a like.
                eachpost.likes.add(request.user)
                # If the user has disliked this post, remove the dislike.
                if request.user in eachpost.dislikes.iterator():
                    eachpost.dislikes.remove(request.user)
        else:
            # If the user has already disliked this post, remove the dislike.
            if request.user in eachpost.dislikes.iterator():
                eachpost.dislikes.remove(request.user)
            else:
                # Otherwise, add a dislike.
                eachpost.dislikes.add(request.user)
                # If the user has liked this post, remove the like.
                if request.user in eachpost.likes.iterator():
                    eachpost.likes.remove(request.user)

        # Save the changes to the database
        eachpost.save()

        # Return a JSON response with the new like and dislike counts
        return JsonResponse({'likes': eachpost.likes.count(), 'dislikes': eachpost.dislikes.count()})

    else:
        eachpost = get_object_or_404(Blog, slug=post_name)
        context = {'eachpost': eachpost,
                   'post_name': post_name}

        return render(request, 'showcase:likes.html', context)


from django.shortcuts import get_object_or_404, redirect, render
from .forms import FeedbackForm
from .models import Item, OrderItem, Feedback

from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import FeedbackForm
from .models import Item, OrderItem, Feedback

"""
class SubmitFeedbackView(DetailView):
   template_name = "review_detail.html"
   form_class = FeedbackForm
   success_url = '/feedbackfinish'
   paginate_by = 10

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
       context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
       context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
       context['Feed'] = Feedback.objects.filter(is_active=1, feedbackpage=self.template_name).order_by("slug")
       context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
       context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
       context['TextFielde'] = TextBase.objects.filter(page=self.template_name).order_by("section")
       return context

   def get_form_kwargs(self):
       kwargs = super().get_form_kwargs()
       kwargs['request'] = self.request
       return kwargs

   def get(self, request, orderitem_id):
       order_item = get_object_or_404(OrderItem, id=orderitem_id, user=request.user)
       form = FeedbackForm(request=request, initial={'order_item': order_item})
       return render(request, 'create_review.html', {'form': form})

   def form_valid(self, form):
       orderitem_id = self.kwargs['orderitem_id']
       order_item = get_object_or_404(OrderItem, id=orderitem_id, user=self.request.user)

       feedback = form.save(commit=False)
       feedback.username = self.request.user.username
       feedback.order = order_item
       feedback.slug = order_item.slug
       feedback.item = order_item.item
       feedback.save()

       messages.success(self.request, 'Your feedback has been submitted successfully.')
       return redirect(self.success_url)

   def form_invalid(self, form):
       messages.error(self.request, 'Invalid form data.')
       return render(self.request, 'create_review.html', {'form': form})"""

from django.shortcuts import get_object_or_404

"""
def submit_feedback(request, item_id):
   item = get_object_or_404(Item, id=item_id)
   user = request.user
   order_items = OrderItem.objects.filter(user=user, item=item).first()  # Filter order items by user and item

   if request.method == 'POST':
       form = FeedbackForm(request.POST, request=request)
       if form.is_valid():
           feedback = form.save(commit=False)
           feedback.username = user.username
           feedback.slug = order_item.slug  # Consider changing this line to feedback.slug = order_item.first().slug
           feedback.item = item
           feedback.order = order_item.first()  # Use order_item.first() to get the first matching order item
           feedback.save()
           messages.success(request, 'Your feedback has been submitted successfully.')
           return redirect('showcase:feedbackfinish')
       else:
           messages.error(request, "Invalid form data.")
   else:
       form = FeedbackForm(request=request)

   # Add the form and order_items to the context
   context = {
       'form': form,
       'order_items': order_items,
   }

   return render(request, 'create_review.html', context)"""

"""
def submit_feedback(request, item_id):
   item = get_object_or_404(Item, id=item_id)
   user = request.user
   order_item = get_object_or_404(OrderItem, user=user, item=item)

   if request.method == 'POST':
       form = FeedbackForm(request.POST, request=request)
       if form.is_valid():
           feedback = form.save(commit=False)
           feedback.username = user
           feedback.slug = order_item.slug
           feedback.item = item
           feedback.order = order_item
           feedback.save()
           messages.success(request, 'Your feedback has been submitted successfully.')
           return redirect('showcase:feedbackfinish')
       else:
           messages.error(request, "Invalid form data.")
   else:
       form = FeedbackForm(request=request)

   return render(request, 'create_review.html', {'form': form})
"""

from django.shortcuts import render, get_object_or_404, redirect
from .models import OrderItem, Feedback
from .forms import FeedbackForm  # Assuming you have a feedback form defined

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Feedback, Item, OrderItem
from .forms import FeedbackForm

from django.shortcuts import render, redirect
from .forms import FeedbackForm

from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import OrderItem, Feedback

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormMixin
from .models import Feedback, OrderItem
from .forms import FeedbackForm
from .models import (
    LogoBase,
    BaseCopyrightTextField,
    Titled,
    FaviconBase,
    NavBarHeader,
    NavBar,
    BackgroundImageBase,
)


class CreateReviewView(LoginRequiredMixin, FormView):
    template_name = "create_review.html"
    form_class = FeedbackForm

    def get(self, request, *args, **kwargs):
        item_slug = request.GET.get('item_slug')
        orderitem_id = request.GET.get('orderitem_id')

        try:
            orderitem = OrderItem.objects.get(id=orderitem_id)
        except OrderItem.DoesNotExist:
            return HttpResponse('Sorry, this order does not exist.')

        # Set the 'item' and 'slug' fields based on the order item
        if orderitem.item:
            initial = {
                'item': orderitem.item,
                'slug': orderitem.slug,
                'order': orderitem,
            }
        else:
            initial = {'slug': orderitem.slug}

        # Create an instance of the FeedbackForm and pass the initial data
        form = FeedbackForm(initial=initial, request=request)

        context = self.get_context_data(form=form)

        return render(request, 'create_review.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(is_active=1, page=self.template_name).order_by(
            "position")
        # context['TextFielde'] = TextBase.objects.filter(is_active=1,page=self.template_name).order_by("section")
        context['Titles'] = Titled.objects.filter(is_active=1, page=self.template_name).order_by("position")
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Profile'] = UpdateProfile.objects.all()
        context['Logo'] = LogoBase.objects.all()
        context['Favicons'] = FaviconBase.objects.filter(is_active=1)

        return context

    def post(self, request, *args, **kwargs):
        item_slug = request.GET.get('item_slug')
        orderitem_id = request.GET.get('orderitem_id')

        try:
            orderitem = OrderItem.objects.get(id=orderitem_id)
        except OrderItem.DoesNotExist:
            return redirect('showcase:ehome')

        try:
            existing_feedback = Feedback.objects.get(order=orderitem)
        except Feedback.DoesNotExist:
            existing_feedback = None

        # Create or update the feedback instance
        form = FeedbackForm(request.POST, request.FILES, request=request, instance=existing_feedback)

        if form.is_valid():
            feedback = form.save(commit=False)

            # Set the 'item' field based on the order item
            feedback.item = orderitem.item  # Assuming 'item' is a ForeignKey in Feedback

            # Set other fields
            feedback.username = request.user if request.user.is_authenticated else None
            feedback.order = orderitem
            feedback.slug = orderitem.slug

            # Automatically set the user, item, and order fields
            if request.user.is_authenticated:
                feedback.username = request.user
            else:
                feedback.username = None

            feedback.item = orderitem.item
            feedback.order = orderitem

            feedback.save()

            if existing_feedback and existing_feedback != feedback:
                existing_feedback.delete()
                slug = str(existing_feedback.slug)
            else:
                slug = str(feedback.slug)

            url = reverse('showcase:review_detail', args=[slug])
            return redirect(url)

        else:
            context = self.get_context_data(form=form)
            return render(request, 'create_review.html', context)

        return render(request, 'create_review.html', {'form': form})


from .forms import FeedForm


class FeedView(FormMixin, ListView):
    model = Feedback
    template_name = "create_review.html"
    form_class = FeedForm

    def get_context_data(self, **kwargs):
        print("get_context_data is being called")
        context = {
            'Logo': LogoBase.objects.filter(page=self.template_name, is_active=1).order_by("section"),
            'BaseCopyrightTextFielded': BaseCopyrightTextField.objects.filter(is_active=1),
            'Titles': Titled.objects.filter(is_active=1, page=self.template_name).order_by("position"),
            'Favicons': FaviconBase.objects.filter(is_active=1),
            'Header': NavBarHeader.objects.filter(is_active=1).order_by("row"),
            'DropDown': NavBar.objects.filter(is_active=1).order_by('position'),
            'Background': BackgroundImageBase.objects.filter(is_active=1)
        }
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = FeedForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.user = request.user
            post.save()
            messages.success(request, 'Form submitted successfully.')
            url = reverse('showcase:review_detail', args=[slug])
            return redirect(url)
        else:
            print(form.errors)
            print(form.non_field_errors())
            print(form.cleaned_data)
            messages.error(request, "Form submission invalid")
            return render(request, "create_review.html", {'form': form})


@login_required(login_url='/accounts/login/')
def submit_feedback(request):
    user = request.user

    if request.method == 'POST':
        form = FeedbackForm(request=request, item=item, orderitem=orderitem)
        if form.is_valid():
            star_rating = form.cleaned_data['star_rating']
            comment = form.cleaned_data['comment']

            # Update or create feedback
            feedback, created = Feedback.objects.update_or_create(
                username=request.user,
                # Use request.user.username to get the currently logged-in user's username
                defaults={'star_rating': star_rating, 'comment': comment}
            )

            # Redirect to a thank-you page or some other appropriate view
            return redirect('showcase:feedbackfinish')  # Change this to your desired URL

    else:
        # If the request method is GET, create a new feedback form
        form = FeedbackForm(request=request)

    return render(request, 'create_review.html', {'form': form})


def edit_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)

    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback, request=request)
        if form.is_valid():
            form.save()
            return redirect('showcase:create_review')
    else:
        form = FeedbackForm(instance=feedback, request=request)

    return render(request, 'create_review.html', {'form': form})


@login_required(login_url='/accounts/login/')
def submit_feedback(request):
    user = request.user

    if request.method == 'POST':
        form = FeedbackForm(request.POST, request=request)
        if form.is_valid():
            star_rating = form.cleaned_data['star_rating']
            comment = form.cleaned_data['comment']

            # Update or create feedback
            feedback, created = Feedback.objects.update_or_create(
                username=request.user,
                # Use request.user.username to get the currently logged-in user's username
                defaults={'star_rating': star_rating, 'comment': comment}
            )

            # Redirect to a thank-you page or some other appropriate view
            return redirect('showcase:feedbackfinish')  # Change this to your desired URL

    else:
        # If the request method is GET, create a new feedback form
        form = FeedbackForm(request=request)

    return render(request, 'create_review.html', {'form': form})


def edit_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)

    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback, request=request)
        if form.is_valid():
            form.save()
            return redirect('showcase:create_review')
    else:
        form = FeedbackForm(instance=feedback, request=request)

    return render(request, 'create_review.html', {'form': form})


from django.utils.text import slugify
from urllib.parse import quote


@login_required
def my_order_items(request):
    user = request.user
    order_items = OrderItem.objects.filter(user=user)
    context = {'order_items': order_items}
    return render(request, 'order_history.html', context)


class OrderHistory(ListView):
    model = Order
    template_name = "order_history.html"
    context_object_name = 'order'

    def get_context_data(self, **kwargs):

        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['Header'] = NavBarHeader.objects.filter(is_active=1).order_by("row")
        context['DropDown'] = NavBar.objects.filter(is_active=1).order_by('position')
        context['Logo'] = LogoBase.objects.filter(page=self.template_name, is_active=1)
        context['Feed'] = Feedback.objects.filter(is_active=1, feedbackpage=self.template_name).order_by("slug")
        context['BaseCopyrightTextFielded'] = BaseCopyrightTextField.objects.filter(is_active=1)
        context['Background'] = BackgroundImageBase.objects.filter(page=self.template_name).order_by("position")
        context['items'] = Item.objects.all()
        context['feedback'] = Feedback.objects.all()
        # context['orders'] = OrderItem.objects.filter(user=self.request.user)
        print(user)

        # Retrieve the author's profile avatar
        items = Item.objects.filter(is_active=1)

        context['Iteme'] = items

        # Iterate over each item in 'Iteme'
        for items in context['Iteme']:
            # Get the image of the item
            image = items.image
            # Check if the user is authenticated
            if user.is_authenticated:
                # Try to get the first profile detail of the current user
                profile = ProfileDetails.objects.filter(user=user).first()
                # If a profile detail exists
                if profile:
                    # Update the author's profile picture URL in the item
                    items.author_profile_picture_url = profile.avatar.url
                    # Update the author's profile URL in the item
                    items.author_profile_url = items.get_profile_url()
            else:
                # Handle the case when the user is not authenticated
                messages.warning(self.request, "You need to log in")
                return redirect("accounts/login")  # replace "login" with your login route

        order = OrderItem.objects.filter(is_active=1, user=user)
        context['orders'] = order
        total_items = OrderItem.objects.filter(is_active=1).count()

        # Get the paginate_by value from the form data or settings
        paginate_by = int(self.request.GET.get('paginate_by', settings.DEFAULT_PAGINATE_BY))

        items_query = OrderItem.objects.filter(is_active=1)
        paginator = Paginator(items_query, paginate_by)
        page_number = self.request.GET.get('page')
        paginated_items = paginator.get_page(page_number)

        # context['items'] = paginated_items

        # context['items'] = Item.objects.filter(is_active=1)

        context['orders'] = paginated_items
        for order_item in context['orders']:
            # Process each order item individually
            image = order_item.image  # Assuming OrderItem has an 'image' field
            user = self.request.user
            profile = ProfileDetails.objects.filter(user=user).first()  # Fetch the profile for the current user

            if order_item.image:
                order_item.image_url = order_item.image.url

            order_item.author_profile_url = order_item.get_profile_url() if order_item.get_profile_url() else None
            order_item.hyperlink = order_item.get_profile_url()  # Example, adjust this as needed

            if profile:
                order_item.author_profile_picture_url = profile.avatar.url
                order_item.profile_url = order_item.get_profile_url2()

        return context


from django.forms import formset_factory
from .models import Questionaire
from .forms import QuestionCountForm, QuestionForm


def get_num_questions(request, question_id):
    if request.method == 'POST':
        form = QuestionCountForm(request.POST)
        if form.is_valid():
            num_questions = form.cleaned_data['num_questions']
            # Redirect to a view to create questions based on num_questions
            return HttpResponseRedirect(reverse('showcase:create_questions', args=[num_questions]))
    else:
        form = QuestionCountForm()
    return render(request, 'get_num_questions.html', {'form': form})


from django.forms import formset_factory, modelformset_factory


@login_required  # previous
def create_questioned(request, num_questions):
    QuestionFormSet = formset_factory(QuestionForm, extra=num_questions)

    if request.method == 'POST':
        formset = QuestionFormSet(request.POST, prefix='question')
        if formset.is_valid():
            user = request.user  # Get the currently logged-in user
            for form in formset:
                text = form.cleaned_data['text']
                Questionaire.objects.create(user=user, text=text)  # Associate the user with the question
            return HttpResponseRedirect(reverse('showcase:index'))
    else:
        formset = QuestionFormSet(prefix='question')

    return render(request, 'create_questions.html', {'formset': formset})


@login_required
def create_questions(request, num_questions):
    if request.method == 'POST':
        FormSet = modelformset_factory(
            Questionaire,
            fields=('text', 'form_type', 'answer_choices'),  # Include answer_choices
            extra=num_questions,
        )
        formset = FormSet(request.POST, prefix='question')

        if formset.is_valid():
            user = request.user
            instances = formset.save(commit=False)

            # Process answer_choices for multiple-choice questions
            for form, instance in zip(formset, instances):
                if instance.form_type == 'option1':
                    answer_choices = form.cleaned_data.get('answer_choices', '').split(',')
                    instance.answer_choices = answer_choices
                instance.user = user
                instance.save()

            return HttpResponseRedirect(reverse('showcase:index'))
    else:
        FormSet = modelformset_factory(
            Questionaire,
            fields=('text', 'form_type', 'answer_choices'),  # Include answer_choices
            extra=num_questions,
        )
        formset = FormSet(queryset=Questionaire.objects.none(), prefix='question')

    return render(request, 'create_questions.html', {'formset': formset})


def add_question(request):
    QuestionAnswerFormSet = formset_factory(AnswerForm, extra=2, can_delete=True)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        formset = QuestionAnswerFormSet(request.POST, prefix='answer')

        if question_form.is_valid() and formset.is_valid():
            # Handle saving question and answers here
            # You can access question_form.cleaned_data['question']
            # and iterate through formset.cleaned_data to get answer choices
            # Save the question and its answer choices to the database

            return redirect('showcase:index')
    else:
        question_form = QuestionForm()
        formset = QuestionAnswerFormSet(prefix='answer')

    return render(request, 'add_question.html', {'question_form': question_form, 'formset': formset})


"""
def create_questionaire(request, num_questions):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # Save the question with answer choices
            questionaire = form.save(commit=False)
            answer_choices = request.POST.getlist('answer_choices')
            questionaire.answer_choices = answer_choices
            questionaire.save()
            return redirect('showcase:index')
    else:
        form = QuestionForm()
    return render(request, 'create_questions.html', {'form': form})
"""


def submit_answer(request, question_id):
    questionaire = get_object_or_404(Questionaire, pk=question_id)
    questions = questionaire.question_set.all()

    if request.method == 'POST':
        form = AnswerForm(request.POST, questions=questions)

        if form.is_valid():
            # Handle the submitted answers here
            for question in questions:
                answer_text = form.cleaned_data[f'answer_{question.id}']
                correct_answer = getattr(questionaire, f'correct_answer_{question.form_type}')
                is_correct = answer_text == correct_answer
                # Save the answer and correctness status to the database or perform any necessary processing

            # Redirect or render a success page
            return HttpResponseRedirect(reverse('showcase:index'))
    else:
        form = AnswerForm(questions=questions)

    return render(request, 'showcase/answer_questions.html', {'form': form})


def sociallogin(request):
    return render(request, 'registration/sociallogin.html')
