from datetime import timezone, timedelta, date
from urllib import request

import self
from django import forms
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404

from mysite import settings
from .models import Idea, OrderItem, EmailField, Item, Questionaire, StoreViewType, LotteryTickets, Meme, TradeOffer, \
    FriendRequest, Game, CurrencyOrder, UploadACard, Room, InviteCode, InventoryObject, CommerceExchange, ExchangePrize, \
    Trade_In_Cards, DegeneratePlaylistLibrary, DegeneratePlaylist, Choice, CATEGORY_CHOICES, CONDITION_CHOICES, \
    SPECIAL_CHOICES, QuickItem, SpinPreference, TradeItem, PrizePool
from .models import UpdateProfile
from .models import Vote
from .models import StaffApplication
from .models import PartnerApplication
from .models import PunishmentAppeal
from .models import BanAppeal
from .models import ReportIssue
from .models import Shuffler
from .models import NewsFeed
from .models import StaffProfile
from .models import Event
from .models import Comment
from .models import Contact
from .models import BusinessMailingContact
from .models import ProfileDetails
from .models import UserProfile2
from .models import Support
from .models import SettingsModel
from .models import BackgroundImage
from .models import EBackgroundImage
from .models import ShowcaseBackgroundImage
from .models import ChatBackgroundImage
from .models import BilletBackgroundImage
from .models import BlogBackgroundImage
from .models import PostBackgroundImage
from .models import RuleBackgroundImage
from .models import AboutBackgroundImage
from .models import FaqBackgroundImage
from .models import StaffBackgroundImage
from .models import InformationBackgroundImage
from .models import TagBackgroundImage
from .models import UserBackgroundImage
from .models import StaffRanksBackgroundImage
from .models import MegaBackgroundImage
from .models import EventBackgroundImage
from .models import NewsBackgroundImage
from .models import BaseCopyrightTextField
from .models import Battle
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import CheckboxSelectMultiple

# from .models import ProfileTwo
# from .models import PublicProfile
users = User.objects.filter()


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '150 Characters or fewer. Letters, digits and @/./+/-/_ only.'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your email address'}))
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your password must be at least 8 characters.'}), label='Password')
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please confirm your password.'}),
                                label='Confirm Password')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


CONTACT_PREFERENCE = [
    ('email', 'Email'),
    ('chat', 'Chat'),
    ('call', 'Call'),
]


class ContactForm(forms.ModelForm):
    prefered_contact = forms.MultipleChoiceField(choices=CONTACT_PREFERENCE, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Contact
        fields = '__all__'


class BusinessContactForm(forms.ModelForm):
    prefered_contact = forms.MultipleChoiceField(choices=CONTACT_PREFERENCE, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = BusinessMailingContact
        fields = '__all__'


class PostForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your name.'}))
    description = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your profile description.'}))

    class Meta:
        model = UpdateProfile
        fields = ('name', 'description', 'image')
        # name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your first name'}))

        # description = forms.CharField(widget = forms.EmailInput
        # (attrs={'placeholder':'Enter your email'}))


class Postit(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your name.'}))
    category = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Choose a category you want your idea to affect.'}))
    description = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please share any ideas you may have.'}))

    class Meta:
        model = Idea
        fields = ('name', 'category', 'description', 'image')


class PosteForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Liam Mannara'}))
    category = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Choose a category you want your vote to affect.'}))

    # altered image URLField to ImageField, check for bugs please

    class Meta:
        model = Vote
        fields = ('name', 'category')


# Profile Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


"""class ReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Write Your Review Here"}))

    class Meta:
        model = ProductReview
        fields = '__all__'"""


class ShippingForm(forms.ModelForm):
    class Meta:
        model = UserProfile2
        fields = ('address', 'city', 'state', 'phone_number', 'profile_picture')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ShippingForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = False
        self.fields['profile_picture'].required = False
        self.user = user

    def save(self, commit=True):
        user_profile = super().save(commit=False)
        user_profile.city = self.cleaned_data['city']
        user_profile.state = self.cleaned_data['state']
        user_profile.phone_number = self.cleaned_data['phone_number']
        user_profile.profile_picture = self.cleaned_data['profile_picture']
        if commit:
            if hasattr(self.user, 'userprofile2') and self.user.userprofile2.exists():
                user_profile.save()
            else:
                user_profile.user = self.user
                user_profile.save()
        return user_profile


class StaffJoin(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Lemon Sauce'}))
    role = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'What role are you applying for?'}))
    I_have_no_strikes_on_my_account_currently = forms.BooleanField()
    Why_do_you_want_to_apply_for_staff = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Tell us why you want to be a Accomfort Staff Member. Be descriptive.'}),
        label='Why do you want to apply for staff?'
    )
    How_do_you_think_you_can_make_PokeTrove_better = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Tell us what you will do to make Accomfort better as a staff member.'}),
        label='How do you think you can make PokeTrove better?'
    )
    I_confirm_that_I_have_read_all_the_staff_requirements_and_meet_all_of_them = forms.BooleanField(
        label='I confirm that I have read all the staff requirements and meet all of them'
    )

    class Meta:
        model = StaffApplication
        fields = ('name', 'role', 'I_have_no_strikes_on_my_account_currently',
                  'Why_do_you_want_to_apply_for_staff',
                  'overall_time_check', 'previous_role_time_check',
                  'How_do_you_think_you_can_make_PokeTrove_better',
                  'I_confirm_that_I_have_read_all_the_staff_requirements_and_meet_all_of_them')


class Server_Partner(forms.ModelForm):
    class Meta:
        model = PartnerApplication
        fields = (
            'user', 'name', 'category', 'multi_category', 'description', 'resume', 'requirement_check', 'policy_check',
            'voucher',)


class SupportForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your name.'}))
    category = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please let us know what type of issue you are dealing with.'}))
    issue = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Describe your issue in detail. We will get back to you ASAP.'}))
    additional_comments = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Put any additional comments you may have here.'}))

    class Meta:
        model = Support
        fields = ('name', 'category', 'issue', 'Additional_comments', 'image',)


class PunishAppeale(forms.ModelForm):
    class Meta:
        model = PunishmentAppeal
        fields = ('name', 'Rule_broken', 'Why_I_should_have_my_punishment_revoked', 'Additional_comments',)


class BanAppeale(forms.ModelForm):
    class Meta:
        model = BanAppeal
        fields = ('name', 'Rule_broken', 'Why_I_should_have_my_ban_revoked', 'Additional_comments',)


class ReportIssues(forms.ModelForm):
    class Meta:
        model = ReportIssue
        fields = ('name', 'category', 'issue', 'Additional_comments', 'image',)


class News_Feed(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Liam_Mannara#6510'}))
    category = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please let us know what form of news this is.'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Write the news here.'}))
    image = forms.FileField(widget=forms.TextInput(attrs={'placeholder': 'Please provide a cover image for the news.'}))

    class Meta:
        model = NewsFeed
        fields = '__all__'


class Staffprofile(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Liam_Mannara#6510'}))
    position = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please let us know what staff position you serve currently.'}))
    description = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Write whatever you want on your profile here (within regulations).'}))
    staff_feats = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Let us know of your transcendental feats of making MegaClan a better place.'}))
    image = forms.FileField(
        widget=forms.TextInput(attrs={'placeholder': 'Please provide a cover image for your profile.'}))

    class Meta:
        model = StaffProfile
        fields = '__all__'


class Eventform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'The event name goes here'}))
    category = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Please let us know what type of event this is (tournament, stage night, etc).'}))
    description = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Give a brief description of the event.'}))
    date_and_time = forms.DateTimeField()
    image = forms.FileField(
        widget=forms.TextInput(attrs={'placeholder': 'Please provide a cover image for the event.'}))

    class Meta:
        model = Event
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'post', 'name', 'email', 'body', 'active'


from django import forms
from django.forms import inlineformset_factory
from .models import Game, Choice


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'file', 'color', 'value', 'category', 'subcategory',]


ChoiceFormSet = inlineformset_factory(
    Game,
    Choice,
    fields=('choice_text', 'file', 'category', 'subcategory'),
    extra=1,  # Number of empty forms to show initially
    can_delete=True,  # Allow users to delete choices
)


#used when the user wants to use their own cards; PokeTrove gets commission
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'cost', 'discount_cost', 'type', 'image', 'power_meter',]


#used when the user wants to use cards owned by PokeTrove; user gets commission

class InventoryGameForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=PrizePool.objects.filter(is_active=1),  # Only active items
        widget=CheckboxSelectMultiple,
        required=False,  # Optional if needed
        label="Available Prizes",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Attach related PrizePool objects to the field choices
        self.fields['items'].choices = [
            (prize.id, prize) for prize in self.fields['items'].queryset
        ]

    def save(self, commit=True):
        # Call the parent save method to create or update the Game instance
        game = super().save(commit=False)
        # Set the player_inventory field to False
        game.player_inventory = False
        if commit:
            # Save the Game instance to the database
            game.save()
            # Save the ManyToMany relationships
            self.save_m2m()
        return game

    class Meta:
        model = Game
        fields = ['name', 'items', 'cost', 'discount_cost', 'type', 'image', 'power_meter']



class CardUploading(forms.ModelForm):
    class Meta:
        model = Choice
        fields = 'choice_text', 'file', 'category', 'tier', 'rarity', 'number_of_choice', 'total_number_of_choice', 'value', 'number'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CardUploading, self).__init__(*args, **kwargs)


ChoiceFormSet = inlineformset_factory(Game, Choice, form=CardUploading, extra=1)


class BattleCreationForm(forms.ModelForm):
    game_values = forms.CharField(
        widget=forms.Textarea(attrs={'readonly': 'readonly'}),
        required=False,
        label="Game Quantities and Values"
    )
    total_value = forms.DecimalField(
        widget=forms.NumberInput(attrs={'readonly': 'readonly'}),
        required=False,
        label="Total Value"
    )

    class Meta:
        model = Battle
        fields = ['battle_name', 'chests', 'min_human_participants', 'game_values', 'total_value']
        widgets = {
            'participants': forms.SelectMultiple(attrs={'disabled': True}),  # Disable participant selection
        }

    def clean(self):
        cleaned_data = super().clean()
        chests = cleaned_data.get('chests')  # This retrieves the M2M data
        battle_instance = self.instance

        if chests:
            # Retrieve the game quantities if the instance exists
            if battle_instance.pk:
                game_quantities = battle_instance.get_game_quantities()
                game_values = [
                    f"{game.name}: {quantity} x {game.cost} = {quantity * game.cost}"
                    for game, quantity in game_quantities.items()
                ]
                total_value = sum(quantity * game.cost for game, quantity in game_quantities.items())
            else:
                # Handle the form without a pre-existing instance
                game_values = [
                    f"{game.name}: 1 x {game.cost} = {game.cost}"
                    for game in chests
                ]
                total_value = sum(game.cost for game in chests)

            cleaned_data['game_values'] = "\n".join(game_values)
            cleaned_data['total_value'] = total_value
        else:
            cleaned_data['game_values'] = ""
            cleaned_data['total_value'] = 0

        return cleaned_data


class BattleJoinForm(forms.Form):
    battle = forms.ModelChoiceField(
        queryset=Battle.objects.filter(status='O'),
        widget=forms.HiddenInput()  # Render as a hidden field
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Pass the user to the form
        battle_instance = kwargs.pop('battle_instance', None)  # Pass the specific battle instance
        super().__init__(*args, **kwargs)

        if battle_instance:
            self.fields['battle'].queryset = Battle.objects.filter(id=battle_instance.id)
            self.fields['battle'].initial = battle_instance

    def clean(self):
        cleaned_data = super().clean()
        battle = cleaned_data.get('battle')

        if not battle:
            raise forms.ValidationError('Battle not selected.')

        # Check if the user is already a participant
        if battle.participants.filter(user=self.user).exists():
            raise forms.ValidationError('You have already joined this battle.')

        # Check if the battle is full
        if battle.participants.count() >= battle.min_human_participants:
            raise forms.ValidationError('This battle has reached the maximum participant limit.')

        return cleaned_data


class MoveToTradeForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    fees = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)
    specialty = forms.ChoiceField(choices=SPECIAL_CHOICES, required=False)
    condition = forms.ChoiceField(choices=CONDITION_CHOICES, initial="M", required=False)
    label = forms.CharField(max_length=1000, required=False)
    slug = forms.SlugField(required=False)
    value = forms.IntegerField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(required=False)
    image_length = forms.IntegerField(required=False)
    image_width = forms.IntegerField(required=False)
    length_for_resize = forms.IntegerField(required=False)
    width_for_resize = forms.IntegerField(required=False)

    class Meta:
        model = TradeItem
        fields = '__all__'


class AddTradeForm(forms.ModelForm):
    class Meta:
        model = InventoryObject
        fields = ('trade_locked',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AddTradeForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['add_trade_item'].queryset = InventoryObject.objects.filter(user=user)


class Trade_In_Form(forms.ModelForm):
    class Meta:
        model = Trade_In_Cards
        fields = ('card_name', 'card_image', 'card_condition',)


# class EditProfileForm(forms.Form):
# username = forms.CharField()
# about_me = forms.CharField(widget=forms.Textarea())
# image = forms.ImageField(required=False)


class SettingsForm(forms.ModelForm):
    class Meta:
        model = SettingsModel
        fields = ('username', 'password', 'email', 'coupons', 'news')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.instance.user
        if commit:
            instance.save()
        return instance


class BaseCopyrightTextFielde(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = BaseCopyrightTextField
        fields = '__all__'


class BackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = BackgroundImage
        fields = '__all__'


class BackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = BackgroundImage
        fields = '__all__'


class EBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = EBackgroundImage
        fields = '__all__'


class ChatBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = ChatBackgroundImage
        fields = '__all__'


class ShowcaseBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = ShowcaseBackgroundImage
        fields = '__all__'


class BlogBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = BlogBackgroundImage
        fields = '__all__'


class PostBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = PostBackgroundImage
        fields = '__all__'


class RuleBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = RuleBackgroundImage
        fields = '__all__'


class AboutBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = AboutBackgroundImage
        fields = '__all__'


class FaqBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = FaqBackgroundImage
        fields = '__all__'


class StaffBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = StaffBackgroundImage
        fields = '__all__'


class InformationBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = InformationBackgroundImage
        fields = '__all__'


class TagBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = TagBackgroundImage
        fields = '__all__'


class UserBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = UserBackgroundImage
        fields = '__all__'


class StaffRanksBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = StaffRanksBackgroundImage
        fields = '__all__'


class MegaBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = MegaBackgroundImage
        fields = '__all__'


class EventBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = EventBackgroundImage
        fields = '__all__'


class NewsBackgroundImagery(forms.ModelForm):
    #    image = forms.ImageField(widget=forms.TextInput(
    #        attrs={'placeholder': 'Link an image for your post.'}))

    class Meta:
        model = NewsBackgroundImage
        fields = '__all__'


class RoomSettings(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['public', 'logo']


class UploadCardsForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name of the card.'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UploadCardsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UploadACard
        fields = ('name', 'image', 'public',)


class InviteCodeForm(forms.ModelForm):
  class Meta:
    model = InviteCode
    fields = ['code', 'user', 'expire_time', 'permalink']  # Assuming these are your fields

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Get the current user if logged in
    user = self.request.user
    if user.is_authenticated:
      self.initial['user'] = user


from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal'),
    ('C', 'Card')
)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(required=False, widget=CountrySelectWidget(attrs={'class': 'custom-select d-block w-100'}))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(required=False, widget=CountrySelectWidget(attrs={'class': 'custom-select d-block w-100'}))
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES, required=True)

    def __init__(self, *args, **kwargs):
        all_items_currency_based = kwargs.pop('all_items_currency_based', False)
        super(CheckoutForm, self).__init__(*args, **kwargs)
        if all_items_currency_based:
            self.fields['payment_option'].required = False
            self.fields['payment_option'].widget = forms.HiddenInput()


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo Code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    email = forms.EmailField()


class PaymentForm(forms.Form):
    number = forms.IntegerField(required=False)
    exp_month = forms.IntegerField(required=False)
    expiry = forms.CharField(required=False)
    exp_year = forms.IntegerField(required=False)
    cvc = forms.IntegerField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


class PaypalPaymentForm(forms.Form):
    # number = forms.IntegerField(required=True)
    number = forms.CharField(required=True)
    exp_month = forms.IntegerField(required=True)
    expiry = forms.CharField(required=True)
    exp_year = forms.IntegerField(required=True)
    cvc = forms.IntegerField(required=True)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


class CurrencyCheckoutForm(forms.Form):
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CurrencyPaymentForm(forms.Form):
    number = forms.IntegerField(required=False)
    exp_month = forms.IntegerField(required=False)
    expiry = forms.CharField(required=False)
    exp_year = forms.IntegerField(required=False)
    cvc = forms.IntegerField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


class CurrencyPaypalPaymentForm(forms.Form):
    # number = forms.IntegerField(required=True)
    number = forms.CharField(required=True)
    exp_month = forms.IntegerField(required=True)
    expiry = forms.CharField(required=True)
    exp_year = forms.IntegerField(required=True)
    cvc = forms.IntegerField(required=True)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


from .models import Withdraw


from django import forms
from .models import Withdraw, InventoryObject


class WithdrawForm(forms.ModelForm):
    selected_cards = forms.ModelMultipleChoiceField(
        queryset=InventoryObject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Withdraw
        fields = ['number_of_cards', 'shipping_state', 'fees', 'status', 'is_active']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['selected_cards'].queryset = InventoryObject.objects.filter(user=user)


class DegeneratePlaylistForm(forms.ModelForm):
    class Meta:
        model = DegeneratePlaylist
        fields = ['user', 'song', 'audio_file', 'audio_img', 'is_active', ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['song'].queryset = DegeneratePlaylistLibrary.objects.filter(user=user)


class TradeProposalForm(forms.ModelForm):
    class Meta:
        model = TradeOffer
        fields = ['title', 'trade_items', 'estimated_trading_value', 'user2', 'message', 'quantity', ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TradeProposalForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['trade_items'].queryset = TradeItem.objects.filter(user=user)


class ExchangePrizesForm(forms.ModelForm):

    class Meta:
        model = CommerceExchange
        fields = ['usercard', 'prizes',] # Adjust fields as needed

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from kwargs (if provided)
        super(ExchangePrizesForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['usercard'].queryset = InventoryObject.objects.filter(user=user)


from .models import Endowment


class EndowmentForm(forms.Form):
    #target = forms.ModelChoiceField(queryset=User.objects.exclude(pk=1))  # Exclude the superuser (with pk=1)
    target = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Name of Endowed Individual'}))  # Exclude the superuser (with pk=1)

    class Meta:
        model = Endowment
        fields = ['user', 'target', 'order']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        #get the current order

        # Set initial values for target and user (optional, adjust as needed)
        self.initial['user'] = self.request.user
        self.initial['target'] = User.objects.exclude(pk=self.request.user.pk).first()

    def clean_user(self):
        username = self.cleaned_data['user']
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            raise forms.ValidationError('Invalid username. Please enter a valid user.')

    def save(self, commit=True):
        instance = Endowment(user=self.cleaned_data['user'], target=self.cleaned_data['target'], order=self.cleaned_data['order'])

        if commit:
            instance.save()

        return instance


class HitStandForm(forms.Form):
    action = forms.ChoiceField(choices=[('hit', 'Hit'), ('stand', 'Stand')], label='Action')


class CreateChest(forms.ModelForm):
    class Meta:
        model = Shuffler
        fields = ('question', 'choice_text', 'file', 'choices', 'category', 'heat', 'shuffletype', 'demonstration',
                  'total_number_of_choice', 'cost',)
        readonly_fields = ('mfg_date',)


from .models import SellerApplication


class SellerApplicationForm(forms.ModelForm):
    class Meta:
        model = SellerApplication
        fields = ['first_name', 'last_name', 'age', 'identification', 'email']

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('age')
        today = date.today()
        if (today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))) < 18:
            raise ValidationError('You need to be 18 or older to apply to sell!')
        return dob


class ProfileDetail(forms.ModelForm):
    class Meta:
        model = ProfileDetails
        fields = ('email', 'avatar', 'alternate', 'about_me')


class StoreViewTypeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = StoreViewType
        fields = ('type',)

    def save(self, commit=True):

        user = self.request.user if self.request.user.is_authenticated else None

        storeviewtype = super().save(commit=False)

        # Set the user, star rating, and slug if available
        if user and isinstance(user, User):  # Check if user is a User instance
            storeviewtype.user = user
        else:
            storeviewtype.user = None  # Set to None if user is not a valid User instance

        if commit:
            storeviewtype.save()
        return storeviewtype


# class PublicForm(forms.ModelForm):
# class Meta:
# model = PublicProfile
# fields = ['username']


# class NewUserForm(UserCreationForm):
# ...

# class UserForm(forms.ModelForm):
# ...

# class ProfileForm(forms.ModelForm):
# class Meta:
# model = ProfileTwo
# fields = ('products',)


from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data["new_password1"]

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password',)


class BilletBackgroundImagery(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam Mannara'}))
    category = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Choose a category you want your idea to affect.'
        }))
    image = forms.ImageField(widget=forms.TextInput(
        attrs={'placeholder': 'Attach an image for your post.'}))

    class Meta:
        model = BilletBackgroundImage
        fields = '__all__'


class TagBackgroundImagery(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'e.g. Liam Mannara'}))
    category = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Choose a category you want your idea to affect.'
        }))
    image = forms.ImageField(widget=forms.TextInput(
        attrs={'placeholder': 'Attach an image for your post.'}))

    class Meta:
        model = TagBackgroundImage
        fields = '__all__'


class StaffRanksBackgroundImagery(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Liam Mannara'}))
    category = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Choose a category you want your idea to affect.'}))
    image = forms.ImageField(widget=forms.TextInput(attrs={'placeholder': 'Attach an image for your post.'}))

    class Meta:
        model = StaffRanksBackgroundImage
        fields = '__all__'


class MegaBackgroundImagery(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Liam Mannara'}))
    category = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Choose a category you want your idea to affect.'}))
    image = forms.ImageField(widget=forms.TextInput(attrs={'placeholder': 'Attach an image for your post.'}))

    class Meta:
        model = MegaBackgroundImage
        fields = '__all__'


from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group

User = get_user_model()


# Create ModelForm based on the Group model.
class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    # Add the users field.
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        # Use the pretty 'filter_horizontal widget'.
        widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance


from django.core.mail import send_mail


class ContactForme(forms.ModelForm):
    class Meta:
        model = Contact
        fields = {"name", "email", "inquiry", "message"}

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'e.g. Marinara Sauce'}),
            "email": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'e.g. Intellex@gmail.com'}),
            "inquiry": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Subject of your message.'}),
            "message": forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Your message.'})
        }

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('inquiry')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg, from_email

    def send(self):
        subject, msg, from_email = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=from_email,
            recipient_list=[settings.EMAIL_HOST_USER]
        )


class BusinessMailingForm(forms.ModelForm):
    class Meta:
        model = BusinessMailingContact
        fields = {"name", "email", "inquiry", "message"}

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'e.g. Liam Mannara'}),
            # get this instead of Contact.name in views
            "email": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'e.g. Intellex@gmail.com'}),
            "inquiry": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Your inquiry goes here.'}),
            "message": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Your message goes here.'})
        }

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('inquiry')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg, from_email

    def send(self):
        subject, msg, to_email = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email]
        )


from .models import Feedback

from django.contrib import admin
from django.contrib.auth.models import User


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('user', 'item', 'quantity', 'slug')
        # might want to replace item with order (check models)
        widgets = {
            # 'slug': forms.TextInput(attrs={'readonly': 'readonly'})
        }


class OrderItemAdmin(admin.ModelAdmin):
    form = OrderItemForm
    # readonly_fields = ('user', 'slug', 'item', 'quantity')


admin.site.register(OrderItem, OrderItemAdmin)

from .models import Wager


class WagerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user_profile = kwargs.pop('user_profile', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Wager
        fields = ['amount']

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if self.user_profile and self.user_profile.currency_amount < amount:
            raise forms.ValidationError("Insufficient funds for this bet.")
        return amount


class DirectedTradeOfferForm(forms.ModelForm):
    class Meta:
        model = TradeOffer
        fields = ['trade_status']  # or any other fields you want in the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trade_status'].widget = forms.RadioSelect(choices=TradeOffer.TRADE_STATUS)

    def clean_direct_trade_offer(self):
        user = self.instance.user
        return user


class TradeOfferAcceptanceForm(forms.ModelForm):
    class Meta:
        model = TradeOffer
        fields = ['user', 'user2']


from django.core.exceptions import ValidationError


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'title', 'price', 'discount_price', 'specialty', 'label', 'slug', 'description', 'image')
        widgets = {
            # 'slug': forms.TextInput(attrs={'readonly': 'readonly'})
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        user = self.instance.user
        if Item.objects.filter(title=title, user=user).exists():
            raise ValidationError("You have already created an item with this title.")
        return title

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        discount_price = cleaned_data.get('discount_price')

        if discount_price is not None:
            fees = discount_price * 0.07
        else:
            fees = price * 0.07

        cleaned_data['fees'] = fees

        return cleaned_data


class QuickItemForm(forms.ModelForm):
    class Meta:
        model = QuickItem
        fields = ['image', 'image_length', 'image_width']


from .models import TradeItem

from .models import TradeOffer


class TradeItemForm(forms.ModelForm):
    class Meta:
        model = TradeItem
        fields = ['title', 'category', 'specialty', 'condition', 'slug', 'status', 'description', 'image']


class TradeProposalForm(forms.ModelForm):
    class Meta:
        model = TradeOffer
        fields = ['title', 'trade_items', 'estimated_trading_value', 'user2', 'message', 'quantity', ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TradeProposalForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['trade_items'].queryset = TradeItem.objects.filter(user=user)


class FriendRequestForm(forms.ModelForm):
    receiver = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'You can add friends with their username.'}))

    class Meta:
        model = FriendRequest
        fields = ['receiver']  # or any other fields you want in the form

    def clean_receiver(self):
        receiver_username = self.cleaned_data['receiver']
        try:
            receiver = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            raise ValidationError("User with this username does not exist.")
        return receiver


class FriendRequestAcceptanceForm(forms.ModelForm):
    class Meta:
        model = FriendRequest
        fields = ['sender', 'receiver']


from django import forms
from .models import RespondingTradeOffer, TradeOffer

from django.contrib.auth.decorators import login_required

# forms.py
from django import forms
from .models import TradeItem, RespondingTradeOffer

from .fields import UserRestrictedModelMultipleChoiceField


class RespondingTradeOfferForm(forms.ModelForm):
    offered_trade_items = UserRestrictedModelMultipleChoiceField(user=None, required=False)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['offered_trade_items'].queryset = TradeItem.objects.filter(user=user)
        self.fields['offered_trade_items'].user = user

    class Meta:
        model = RespondingTradeOffer
        fields = ['estimated_trading_value', 'offered_trade_items', 'wanted_trade_items', 'message']


from django.utils import timezone


class TicketRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TicketRequestForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        user = self.user

        # Get the current time and the time at 5pm of the previous day
        now = timezone.now()  # Use timezone.now() instead of datetime.timezone.now()
        reset_time = now.replace(hour=17, minute=0, second=0)
        if now.hour < 17:
            reset_time -= timedelta(days=1)

        # Check if the user has already submitted a form since the reset time
        if LotteryTickets.objects.filter(user=user, mfg_date__gte=reset_time).exists():
            raise forms.ValidationError("You have already collected your daily ticket. Please try again after 5pm.")

        return cleaned_data

    class Meta:
        model = LotteryTickets
        fields = ('name',)


from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import get_user_model
from .models import Feedback

"""class FeedbackForm(forms.ModelForm):
    star_rating = forms.ChoiceField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    comment = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Outstanding!'}))
    order = forms.ModelChoiceField(queryset=None)
    image = forms.ImageField(required=False)

    class Meta:
        model = Feedback
        fields = ('order', 'star_rating', 'comment', 'slug', 'image')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(initial=self.request.user.username)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['order'].queryset = OrderItem.objects.filter(user=self.request.user)

"""

from django import forms
from .models import Feedback
from .models import OrderItem

from django import forms
from django.utils.text import slugify
from django import forms
from .models import Feedback
from django import forms

from django import forms
from .models import Feedback

from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Feedback
        fields = ('order', 'star_rating', 'comment', 'slug', 'image')

    def save(self, commit=True):
        # Get the user who created the feedback
        user = self.request.user if self.request.user.is_authenticated else None

        # Create an instance of the Feedback model
        feedback = super().save(commit=False)

        if feedback.order and feedback.order.item:
            feedback.item = feedback.order.item
        if feedback.order:
            feedback.slug = feedback.order.slug

        # Set the user, star rating, and slug if available
        if user and isinstance(user, User):  # Check if user is a User instance
            feedback.username = user
        else:
            feedback.username = None  # Set to None if user is not a valid User instance

        if 'star_rating' in self.cleaned_data:
            feedback.star_rating = self.cleaned_data['star_rating']
        if 'slug' in self.cleaned_data:
            feedback.slug = self.cleaned_data['slug']

        # Set the 'image' field if an image file is provided
        if 'image' in self.cleaned_data:
            feedback.image = self.cleaned_data['image']

        if commit:
            feedback.save()
        return feedback


class FeedForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('order', 'star_rating', 'comment', 'slug', 'image')


class EmailForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'style': 'height: 50px;'}))

    class Meta:
        model = EmailField
        fields = ('email', 'confirmation')

    def clean_confirmation(self):
        confirmation = self.cleaned_data.get('confirmation')
        if not confirmation:
            raise forms.ValidationError("You must agree to the terms to continue.")
        return confirmation
        # name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your first name'}))

        # description = forms.CharField(widget = forms.EmailInput
        # (attrs={'placeholder':'Enter your email'}))


class SpinPreferenceForm(forms.ModelForm):
    class Meta:
        model = SpinPreference
        fields = ['quick_spin']


class QuestionForm(forms.Form):
    text = forms.CharField(max_length=255)

    answer_choices = forms.MultipleChoiceField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'dynamic-input'}),
        choices=[],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a field for answer choices when the question type is 'Multiple Choice'
        if self.instance.form_type == 'option1':
            self.fields['answer_choices'] = forms.CharField(
                label='Answer Choices (comma-separated)',
                required=True,
                widget=forms.TextInput(attrs={'placeholder': 'Choice 1, Choice 2, ...'}),
            )


class QuestionCountForm(forms.Form):
    num_questions = forms.IntegerField(label="Number of Questions", )
    form_name = forms.CharField()

    class Meta:
        model = Questionaire
        fields = {"form_name", "form_text", "text"}


from .models import Answer


class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', [])
        super(AnswerForm, self).__init__(*args, **kwargs)

        for question in questions:
            field_name = f'answer_{question.id}'
            self.fields[field_name] = forms.CharField(
                label=question.text,
                required=True,
                widget=forms.TextInput(attrs={'class': 'form-control'})
            )


class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['title', 'image']