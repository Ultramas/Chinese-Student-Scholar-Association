from PIL import Image
from django.db import models, migrations
from django.contrib.auth.models import User
from uuid import uuid4
import uuid

from django.dispatch import receiver


# from image.utils import render


# from django.db.models.signals import post_save
from django.conf import settings
from django.db.models import Sum
from django.shortcuts import reverse, get_object_or_404, render
from django_countries.fields import CountryField

CATEGORY_CHOICES = (
   ('G', 'Gold'),
   ('P', 'Platinum'),
   ('E', 'Emerald'),
   ('D', 'Diamond'),
)

LABEL_CHOICES = (
   ('N', 'New'),
   ('BS', 'Best Seller'),
   ('BV', 'Best Value'),
)

TYPE_CHOICES = (('S', 'Singles'), ('BP', 'Booster Pack'),
               ('BB', 'Booster Box'), ('PP', 'Pokemon Product'), ('O',
                                                                  'Other'))

ADDRESS_CHOICES = (
   ('B', 'Billing'),
   ('S', 'Shipping'),
)

class Idea(models.Model):
   """Model for sharing ideas and getting user feedback"""
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=100, help_text='Your name goes here.')
   category = models.CharField(max_length=100,
                               help_text='Choose a category you want your idea to affect (server layout, event idea, etc).')
   description = models.TextField(help_text='Please share any ideas you may have.')
   image = models.ImageField(help_text='Attach an image for your idea (scales to your picture`s dimensions).')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   class Meta:
       verbose_name = "Idea"
       verbose_name_plural = "Ideas"

   def save(self, *args, **kwargs):
       if not self.pk:
           # Get the associated ProfileDetails for the donor
           profile = ProfileDetails.objects.filter(user=self.user).first()

           # Set the position to the position value from the associated ProfileDetails
           if profile:
               self.position = profile.position

       super().save(*args, **kwargs)

   def get_profile_url(self):
       profile = ProfileDetails.objects.filter(user=self.user).first()
       if profile:
           return reverse('showcase:profile', args=[str(profile.pk)])


class UpdateProfile(models.Model):
   """Update user profiles"""
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=100, help_text='Your name goes here.')
   description = models.TextField(help_text='Your profile description goes here.')
   image = models.ImageField(help_text='Attach an image for your profile (scales to your picture`s dimensions.)')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   class Meta:
       verbose_name = "User Profile Post"
       verbose_name_plural = "User Profile Posts"

   def save(self, *args, **kwargs):
       if not self.pk:
           # Get the associated ProfileDetails for the donor
           profile = ProfileDetails.objects.filter(user=self.user).first()

           # Set the position to the position value from the associated ProfileDetails
           if profile:
               self.position = profile.position

       super().save(*args, **kwargs)

   def get_profile_url(self):
       profile = ProfileDetails.objects.filter(user=self.user).first()
       if profile:
           return reverse('showcase:profile', args=[str(profile.pk)])


class Vote(models.Model):
   """Used for voting on different new ideas"""
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=100, help_text='Your name goes here.')
   category = models.CharField(max_length=100,
                               help_text='Type the category that you are voting on (server layout, event idea, administration position, etc).')
   description = models.TextField(help_text='Please share any ideas you may have.')
   image = models.ImageField(help_text='Attach an image for your profile (scales to your picture`s dimensions.)')
   mfg_date = models.DateTimeField(auto_now_add=True)
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   class Meta:
       verbose_name = "Vote"
       verbose_name_plural = "Votes"

   def save(self, *args, **kwargs):
       if not self.pk:
           # Get the associated ProfileDetails for the donor
           profile = ProfileDetails.objects.filter(user=self.user).first()

           # Set the position to the position value from the associated ProfileDetails
           if profile:
               self.position = profile.position

       super().save(*args, **kwargs)

   def get_profile_url(self):
       profile = ProfileDetails.objects.filter(user=self.user).first()
       if profile:
           return reverse('showcase:profile', args=[str(profile.pk)])

class EmailField(models.Model):
    email = models.EmailField(help_text="Sign up for our newsletter to get the latest news and gossip! We will never share your personal information with anyone without your explicit permission. Unsubscribe at any time. ")
    confirmation = models.BooleanField(help_text="By clicking this box, I agree to receive emails, coupons and discounts from PokeTrove. I also understand that I may unsubscribe at any time and PokeTrove will not share my personal information with anyone without my explicit permission.")
    #username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")
    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"

class Product(models.Model):
   """A product in the storefront"""
   name = models.CharField(max_length=200)
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")
   description = models.TextField()
   #label = models.CharField(choices=LABEL_CHOICES, max_length=1000)  # can use for cataloging products
   mfg_date = models.DateTimeField(auto_now_add=True)
   rating = models.CharField(max_length=1, choices=[('b', 'Bad'), ('a', 'Average'), ('e', 'Excellent')])

   def __str__(self):
       return self.name

   def show_desc(self):
       return self.description[:50]


class City(models.Model):
   """Not currently used. NEEDS TO BE DELETED"""
   name = models.CharField(max_length=255)
   state = models.CharField(max_length=255)

   class Meta:
       verbose_name_plural = "Cities"

   def __str__(self):
       return self.name


from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class SearchResult(models.Model):
   content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
   object_id = models.PositiveIntegerField()
   content_object = GenericForeignKey('content_type', 'object_id')
   title = models.CharField(max_length=255)
   description = models.TextField()
   url = models.URLField()


class StaffApplication(models.Model):
   """For applying for staff"""
   name = models.CharField(max_length=100, help_text='Your name & tag go here.')
   overall_time_check = models.BooleanField(
       verbose_name="I have been in MC for at least 2 months",
       default=False,
       choices=((True, 'Yes'), (False, 'No'))
   )
   previous_role_time_check = models.BooleanField(
       verbose_name="I have been in MC for at least 1 month",
       default=False,
       choices=((True, 'Yes'), (False, 'No'))
   )
   meeting_attendance_check = models.BooleanField(
       verbose_name="I can attend at least half of the staff meetings.",
       default=False,
       choices=((True, 'Yes'), (False, 'No'))
   )
   strikes_check = models.BooleanField(
       verbose_name="I have no strikes on my account currently",
       default=False,
       choices=((True, 'Yes'), (False, 'No'))
   )
   role = models.TextField(help_text='What role are you applying for?', verbose_name="Roles")
   why = models.TextField(
       help_text='Tell us why you want to be a MegaClan Staff Member. Be descriptive.',
       verbose_name="Why do you want to apply for staff?"
   )
   how_better = models.TextField(
       help_text='Tell us what you will do to make MC better as a staff member.',
       verbose_name="How do you think you can make MC better?"
   )
   read_requirements = models.BooleanField(
       verbose_name="I confirm that I have read all the staff requirements and meet all of them.",
       default=False,
       choices=((True, 'Yes'), (False, 'No'))
   )
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   class Meta:
       verbose_name = "Staff Application"
       verbose_name_plural = "Staff Applications"


class PartnerApplication(models.Model):
   """Application to partner with the server"""
   name = models.CharField(max_length=100, help_text='Your server name goes here.')
   category = models.CharField(
       max_length=100,
       help_text='Pick a category you feel your server represents (gaming, community, etc).'
   )
   description = models.TextField(help_text='Describe your server. Tell potential members why they should join.')
   server_invite = models.URLField(help_text='Idea your server invite link here.')
   is_active = models.IntegerField(
       default=1,
       blank=True,
       null=True,
       help_text='1->Active, 0->Inactive',
       choices=((1, 'Active'), (0, 'Inactive')),
       verbose_name="Set active?"
   )


class PunishmentAppeal(models.Model):
   name = models.CharField(max_length=100, help_text='Your name and tag go here.')
   Rule_broken = models.CharField(max_length=200,
                                  help_text='Tell us the numbers of the rule(s) you broke. Refer to our rules page to see the rules and their corresponding numbers.',
                                  verbose_name="rule broken: ")
   Why_I_should_have_my_punishment_revoked = models.TextField(
       help_text='Tell us why we should revoke your punishment, and what you can do to fix your mistake. If you think your punishment is a mistake, tell us why.',
       verbose_name="Why I should have my punishment revoked: ")
   Additional_comments = models.TextField(help_text='Put any additional evidence or comments you may have here.',
                                          verbose_name="additional comments ")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   class Meta:
       verbose_name = "Punishment Appeal"
       verbose_name_plural = "Punishment Appeals"


class BanAppeal(models.Model):
   name = models.CharField(max_length=100, help_text='Your name and tag go here.')
   Rule_broken = models.CharField(max_length=200,
                                  help_text='Tell us the numbers of the rule(s) you broke. Refer to our rules page to see the rules and their corresponding numbers.')
   Why_I_should_have_my_ban_revoked = models.TextField(
       help_text='Tell us why we should unban you, and tell us you can do to fix your mistake. If you think your punishment is a mistake, tell us why.',
       verbose_name="Why I should have my ban revoked.")
   Additional_comments = models.TextField(
       help_text='Put any additional evidence or comments you may have here.')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   class Meta:
       verbose_name = "Ban Appeal"
       verbose_name_plural = "Ban Appeals"


class ReportIssue(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=100,
                           help_text='Your name and tag go here. If you wish to stay anonymous, put "Anonymous".')
   category = models.CharField(max_length=200, help_text='Please let us know what type of issue this is.')
   issue = models.TextField(help_text='Describe the issue in detail. We will try to get to it as soon as possible.')
   Additional_comments = models.TextField(help_text='Put any additional comments you may have here.',
                                          verbose_name="additional comments")
   image = models.ImageField(help_text='Please put a screenshot of the issue.')
   anonymous = models.BooleanField(default=False, help_text="Report issue anonymously?")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   # class Changelog(models.Model):
   #  name = models.CharField(max_length = 100, help_text='Your name and tag go here. If you wish to stay anonymous, put "Anonymous".')
   #  category = models.CharField(max_length = 200, help_text='Please let us know what type of issue this is.')
   #  issue = models.TextField(help_text='Describe the issue in detail. We will try to get to it as soon as possible.')
   #  Additional_comments = models.TextField(help_text='Put any additional evidence or comments you may have here.')
   #  image = models.FileField(help_text='Please put a screenshot of the issue.')

   class Meta:
       verbose_name = "Report Issue"
       verbose_name_plural = "Report Issues"

   def save(self, *args, **kwargs):
       if not self.pk:
           # Get the associated ProfileDetails for the donor
           profile = ProfileDetails.objects.filter(user=self.user).first()

           # Set the position to the position value from the associated ProfileDetails
           if profile:
               self.position = profile.position

       super().save(*args, **kwargs)

   def get_profile_url(self):
       profile = ProfileDetails.objects.filter(user=self.user).first()
       if profile:
           return reverse('showcase:profile', args=[str(profile.pk)])


class Support(models.Model):
   name = models.CharField(max_length=100,
                           help_text='Your name and tag go here.')
   category = models.CharField(max_length=200, help_text='Please let us know what type of issue you are dealing with.')
   issue = models.TextField(
       help_text='Describe your issue in detail. We will try to get back to you as soon as possible.')
   Additional_comments = models.TextField(help_text='Put any additional comments you may have here.',
                                          verbose_name="additional comments")
   image = models.ImageField(help_text='Please attach a screenshot of your issue.', null=True, blank=True)
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   class Meta:
       verbose_name = "Customer Support"
       verbose_name_plural = "Customer Support"


class NewsFeed(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=100,
                           help_text='Your name and tag go here. If you wish to stay anonymous, put "Anonymous".')
   slug = models.SlugField(max_length=200, unique=True)
   category = models.CharField(max_length=200, help_text='Please let us know what form of news this is.')
   description = models.TextField(help_text='Write the news here.')
   image = models.ImageField(help_text='Please provide a cover image for the news.')
   date_and_time = models.DateTimeField(null=True, verbose_name="time and date")
   anonymous = models.BooleanField(default=False, help_text="Remain anonymous? (not recommended)")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   class Meta:
       verbose_name = "News Feed"
       verbose_name_plural = "News Feed"

   def save(self, *args, **kwargs):
       if not self.pk:
           # Get the associated ProfileDetails for the donor
           profile = ProfileDetails.objects.filter(user=self.user).first()

           # Set the position to the position value from the associated ProfileDetails
           if profile:
               self.position = profile.position

       super().save(*args, **kwargs)

   def get_absolute_url(self):
       from django.urls import reverse

       return reverse("showcase:news", kwargs={"slug": str(self.slug)})

   def get_profile_url(self):
       profile = ProfileDetails.objects.filter(user=self.user).first()
       if profile:
           return reverse('showcase:profile', args=[str(profile.pk)])


class StaffProfile(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=100,
                           help_text='Your name and tag go here. If you wish to stay anonymous, put "Anonymous".')
   position = models.CharField(max_length=200, help_text='Please let us know what staff position you serve currently.')
   description = models.TextField(help_text='Write whatever you want on your profile here (within regulations).')
   staff_feats = models.TextField(
       help_text='Let us know of your transcendental feats of making MegaClan a better place.',
       verbose_name="staff feats")
   anonymous = models.BooleanField(default=False, help_text="Report issue anonymously?")
   image = models.ImageField(help_text='Please provide a cover image for your profile.')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   class Meta:
       verbose_name = "Staff Profile"
       verbose_name_plural = "Staff Profiles"

   def save(self, *args, **kwargs):
       if not self.pk:
           # Get the associated ProfileDetails for the donor
           profile = ProfileDetails.objects.filter(user=self.user).first()

           # Set the position to the position value from the associated ProfileDetails
           if profile:
               self.position = profile.position

       super().save(*args, **kwargs)

   def get_profile_url(self):
       profile = ProfileDetails.objects.filter(user=self.user).first()
       if profile:
           return reverse('showcase:profile', args=[str(profile.pk)])


class Event(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=100, help_text='Event name goes here.')
   category = models.CharField(max_length=200,
                               help_text='Please let us know what type of event this is (tournament, stage night, etc).')
   description = models.TextField(help_text='Give a brief description of the event.')
   date_and_time = models.DateTimeField(null=True, verbose_name="time and date")
   slug = models.SlugField()
   anonymous = models.BooleanField(default=False, help_text="Remain anonymous? (not recommended)")
   image = models.ImageField(help_text='Please provide a cover image for the event.')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def save(self, *args, **kwargs):
       if not self.pk:
           # Get the associated ProfileDetails for the donor
           profile = ProfileDetails.objects.filter(user=self.user).first()

           # Set the position to the position value from the associated ProfileDetails
           if profile:
               self.position = profile.position

       super().save(*args, **kwargs)

   def get_profile_url(self):
       return reverse('showcase:eventmore', args=[str(self.slug)])

   def get_profile_url2(self):
       profile = ProfileDetails.objects.filter(user=self.user).first()
       if profile:
           return reverse('showcase:profile', args=[str(profile.pk)])


class BusinessMessageBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Business Message Background Image"
       verbose_name_plural = "Business Message Background Images"


class MemberHomeBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Member Home Background Image"
       verbose_name_plural = "Member Home Background Images"


class PatreonBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Patreon Background Image"
       verbose_name_plural = "Patreon Background Images"


class Partner(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=100, help_text='Your server name goes here.')
   category = models.CharField(max_length=100,
                               help_text='Pick a category you feel your server represents (gaming, community, etc).')
   description = models.TextField(help_text='Describe your server. Tell potential members why they should join.')
   server_invite = models.URLField(help_text='Post your server invite link here.')
   anonymous = models.BooleanField(default=False, help_text="Remain anonymous? (not recommended)")

   def save(self, *args, **kwargs):
       if not self.pk:
           # Get the associated ProfileDetails for the donor
           profile = ProfileDetails.objects.filter(user=self.user).first()

           # Set the position to the position value from the associated ProfileDetails
           if profile:
               self.position = profile.position

       super().save(*args, **kwargs)

   def get_profile_url(self):
       profile = ProfileDetails.objects.filter(user=self.user).first()
       if profile:
           return reverse('showcase:profile', args=[str(profile.pk)])


class Patreon(models.Model):
   patreon_username = models.CharField(max_length=100, verbose_name='Patreon`s Username',
                                       help_text='The patreon`s username goes here.')
   description = models.TextField(help_text='Description of Patreon`s patreonage.')
   image = models.ImageField(
       help_text=
       'The patreon`s avatar goes here.')

   # change rest to either imagefields or urlfields (has to be uniform throughout the form)

   # widget=form.TextInput, help_text='Your name goes here.')
   class Meta:
       verbose_name = "Patreon"
       verbose_name_plural = "Patreons"


from django.template.defaultfilters import slugify


class Blog(models.Model):
    """Each blog post"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True, verbose_name="updated on: ")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=((0, "Draft"), (1, "Publish")), default=0)
    image = models.ImageField(upload_to='images/')
    likes = models.ManyToManyField(User, blank=True, verbose_name='post likes')
    # likes = models.IntegerField(default=0)
    dislikes = models.ManyToManyField(User, blank=True, verbose_name='post dislikes', related_name="post_dislikes")
    # url = models.SlugField(max_length=200, unique=True, blank=True)
    # blogbackgroundimage
    is_active = models.IntegerField(default=1,
                                    blank=True,
                                    null=True,
                                    help_text='1->Active, 0->Inactive',
                                    choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ['-created_on']

    #    def save(self, *args, **kwargs):
    #        self.url = slugify(self.title)
    #        super(Blog, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)

        if not self.pk:
            # Get the associated ProfileDetails for the donor
            profile = ProfileDetails.objects.filter(user=self.author_id).first()

            # Set the position to the position value from the associated ProfileDetails
            if profile:
                self.position = profile.position

        super().save(*args, **kwargs)

    def get_profile_url(self):
        profile = ProfileDetails.objects.filter(user=self.author_id).first()
        if profile:
            return reverse('showcase:profile', args=[str(profile.pk)])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("showcase:post_detail", kwargs={"slug": str(self.slug)})

    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    def view_count(self):
        return Blog.objects.filter(post=self).count()

    # def number_of_likes(self):
    #    return self.likes.count()


class Preference(models.Model):
   DoesNotExist = None  # added outside tutorial
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_posts')
   value = models.IntegerField(help_text="1->Like, 2->Dislike")
   date = models.DateTimeField(auto_now=True)

   def __str__(self):
       return str(self.user) + ':' + str(self.post) + ':' + str(self.value)

   class Meta:
       unique_together = ("user", "post", "value")
       verbose_name = "Blog Like"
       verbose_name_plural = "Blog Like"


class Comment(models.Model):
   post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
   name = models.CharField(max_length=80)
   email = models.EmailField()
   body = models.TextField()
   created_on = models.DateTimeField(auto_now_add=True)
   active = models.BooleanField(default=False)
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   class Meta:
       ordering = ['created_on']

   def __str__(self):
       return 'Comment {} by {}'.format(self.body, self.name)

   def get_absolute_url(self):
       from django.urls import reverse

       return reverse("showcase:post_detail", kwargs={"slug": self.post.slug})


class PostLikes(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, )
   post = models.ForeignKey(Idea, on_delete=models.CASCADE, )
   created = models.DateTimeField(auto_now_add=True)

   class Meta:
       verbose_name = "Post Like"
       verbose_name_plural = "Post Likes"


class Profile(models.Model):
   about_me = models.TextField()
   image = models.ImageField(upload_to='profile_image', null=True, blank=True)
   user = models.OneToOneField(User, on_delete=models.CASCADE)

   def __str__(self):
       return str(self.user)


class FaviconBase(models.Model):
   favicontitle = models.TextField(verbose_name="Favicon Title")
   faviconcover = models.ImageField(upload_to='images/', verbose_name="Favicon")
   favicon_length = models.PositiveIntegerField(blank=True, null=True, default="100",
                                                help_text='Original length of the favicon (use for original ratio).',
                                                verbose_name="advertisement length")
   favicon_width = models.PositiveIntegerField(blank=True, null=True, default="100",
                                               help_text='Original width of the favicon (use for original ratio).',
                                               verbose_name="advertisement width")
   length_for_resize = models.PositiveIntegerField(default=40, verbose_name="Resized Length")
   width_for_resize = models.PositiveIntegerField(default=600, verbose_name="Resized Width")
   faviconpage = models.TextField(verbose_name="Page Name")
   faviconurl = models.URLField(verbose_name="Page URL")
   faviconlink = models.TextField(verbose_name="Favicon Link")
   faviconsizes = models.TextField(verbose_name="Favicon Sizes", help_text="example: 180x180")
   faviconrelationship = models.TextField(verbose_name="Favicon Relationship", help_text="example: icon")
   favicontype = models.TextField(verbose_name="Favicon Type", help_text="example: ico")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.favicontitle

   class Meta:
       verbose_name = "Favicon"
       verbose_name_plural = "Favicons"


class LogoBase(models.Model):
   title = models.TextField(verbose_name="Background Title")
   logocover = models.ImageField(upload_to='images/', verbose_name="Logo")
   hyperlink = models.TextField(verbose_name="Hyperlink")
   section = models.IntegerField(verbose_name="Page Section")
   page = models.TextField(verbose_name="Page Name")
   alternate = models.TextField(verbose_name="Alternate Text")
   logo_length = models.PositiveIntegerField(blank=True, null=True, default="100",
                                             help_text='Original length of the advertisement (use for original ratio).',
                                             verbose_name="advertisement length")
   logo_width = models.PositiveIntegerField(blank=True, null=True, default="100",
                                            help_text='Original width of the advertisement (use for original ratio).',
                                            verbose_name="advertisement width")
   length_for_resize = models.PositiveIntegerField(default=40, verbose_name="Resized Length")
   width_for_resize = models.PositiveIntegerField(default=600, verbose_name="Resized Width")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Logo"
       verbose_name_plural = "Logos"


class BackgroundImageBase(models.Model):
   backgroundtitle = models.TextField(verbose_name="Background Title")
   cover = models.ImageField(upload_to='images/')
   page = models.TextField(verbose_name="Page Name")
   url = models.URLField(verbose_name="Page URL")
   position = models.IntegerField(verbose_name="Image Position")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.backgroundtitle

   class Meta:
       verbose_name = "Background Image Base"
       verbose_name_plural = "Background Image Base"


class TextBase(models.Model):
   text = models.TextField(verbose_name="Text")
   page = models.TextField(verbose_name="Page Name")
   url = models.URLField(verbose_name="Page URL")
   header_or_textfield = models.BooleanField(verbose_name="Header or Body Text", default=1,
                                             choices=((1, 'Header'), (0, 'Body')))
   section = models.IntegerField(verbose_name="Text Section", help_text="Section Number of Text")
   exists = models.BooleanField(verbose_name="Section Taken", help_text="Is this section taken?", default=1,
                                choices=((1, 'Yes'), (0, 'No')))
   hyperlink = models.TextField(blank=True, null=True, verbose_name="Hyperlink")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.text

   class Meta:
       verbose_name = "Text Base"
       verbose_name_plural = "Text Base"


class BackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')
   page = models.TextField()
   is_active = models.IntegerField(
       default=1,
       blank=True,
       null=True,
       help_text='1->Active, 0->Inactive',
       choices=((1, 'Active'), (0, 'Inactive')),
       verbose_name="Set active?"
   )

   def __str__(self):
       return self.title

   def save(self, *args, **kwargs):
       if not self.slug:
           slug = self.slug

       super().save(*args, **kwargs)

   def get_profile_url(self):
       return reverse('showcase:profile', args=[str(self.slug)])

   class Meta:
       verbose_name = "Background Image"
       verbose_name_plural = "Background Images"


class ContentBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Content Background Image"
       verbose_name_plural = "Content Background Images"


class SupportBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Support Background Image"
       verbose_name_plural = "Support Background Images"


class ProductBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Product Background Image"
       verbose_name_plural = "Product Background Images"


class NavBar(models.Model):
   text = models.TextField()
   url = models.TextField(blank=True, null=True)
   row = models.IntegerField()
   position = models.IntegerField()
   opennew = models.BooleanField(verbose_name="Open In New Tab?", default=False,
                                 choices=((True, 'Yes'), (False, 'No')))
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.text

   class Meta:
       verbose_name = "Navigational Bar Dropdown"
       verbose_name_plural = "Navigational Bar Dropdowns"


class NavBarHeader(models.Model):
   text = models.TextField(help_text='This is a header.')
   section = models.TextField(max_length=200,
                              blank=True,
                              null=True,
                              help_text='ID Section of page.')
   row = models.IntegerField()
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.text

   class Meta:
       verbose_name = "Navigational Bar Header"
       verbose_name_plural = "Navigational Bar Headers"


from django.contrib.auth.models import AbstractUser


class SettingsModel(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='settings')
   username = models.CharField(help_text='Your username', max_length=200)
   password = models.CharField(help_text='Your password', max_length=200)
   coupons = models.BooleanField(verbose_name="Send me coupons", default=True, blank=True, null=True,
                                 choices=((True, 'Yes'), (False, 'No')))
   news = models.BooleanField(verbose_name="Keep me in the loop", default=True, blank=True, null=True,
                              choices=((True, 'Yes'), (False, 'No')))
   # connects to email
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.username

   class Meta:
       verbose_name = "Setting"
       verbose_name_plural = "Settings"


class Donate(models.Model):
   amount = models.DecimalField(max_digits=10, decimal_places=2)
   timestamp = models.DateTimeField(auto_now_add=True)
   nickname = models.CharField(max_length=100, blank=True, null=True)

   # Add more fields if needed

   # ForeignKey to link each donation to a specific user (donor)
   donor = models.ForeignKey(User, on_delete=models.CASCADE)
   anonymous = models.BooleanField(default=False, help_text="Donate anonymously?")
   # position = models.IntegerField(
   #    default=0,
   #    help_text="Position for sorting",
   #    editable=False,  # This makes the field non-editable in forms
   # )
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return f"Donation by {self.donor} ({self.amount} USD)"

   def save(self, *args, **kwargs):
       if not self.pk:
           # Get the associated ProfileDetails for the donor
           profile = ProfileDetails.objects.filter(user=self.donor).first()

           # Set the position to the position value from the associated ProfileDetails
           if profile:
               self.position = profile.position

       super().save(*args, **kwargs)

   def get_profile_url(self):
       profile = ProfileDetails.objects.filter(user=self.donor).first()
       if profile:
           return reverse('showcase:profile', args=[str(profile.pk)])


class DonorBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')
   donor = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Donors Background Image"
       verbose_name_plural = "Donors Background Images"


class ContributorBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Contributors Background Image"
       verbose_name_plural = "Contributors Background Images"


class SettingsBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Settings Background Image"
       verbose_name_plural = "Settings Background Images"


class DonateIcon(models.Model):
   row = models.IntegerField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Donation Icon"
       verbose_name_plural = "Donation Icons"


class Titled(models.Model):
   overtitle = models.TextField(verbose_name="Title")
   page = models.TextField(verbose_name="Page Name", blank=True, null=True, )
   url = models.URLField(verbose_name="Page URL")
   position = models.IntegerField()
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.overtitle

   class Meta:
       verbose_name = "Page Title"
       verbose_name_plural = "Page Titles"


class SocialMedia(models.Model):
   social = models.TextField(verbose_name="Social Media Platform")
   image = models.ImageField(verbose_name="Social Media Logo")
   image_width = models.PositiveIntegerField(blank=True, null=True, default="100",
                                             help_text='Width of the image (in percent relative).',
                                             verbose_name="image width")
   image_length = models.PositiveIntegerField(blank=True, null=True, default="100",
                                              help_text='Length of the image (in percent relative).',
                                              verbose_name="image length")
   width_for_resize = models.PositiveIntegerField(default=600, verbose_name="Resize Width")
   height_for_resize = models.PositiveIntegerField(default=40, verbose_name="Resize Height")
   image_position = models.IntegerField(help_text='Positioning of the image.', verbose_name='Position')
   alternate = models.TextField(verbose_name="Alternate Text")
   page = models.TextField(verbose_name="Page Name")
   hyperlink = models.TextField(verbose_name="Hyperlink")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.social

   class Meta:
       verbose_name = "Social Media"
       verbose_name_plural = "Social Media"


class BaseCopyrightTextField(models.Model):
   copyright = models.TextField(verbose_name="Copyright Field", help_text="Copyright And Year")
   page = models.TextField(verbose_name="Page Name")
   hyperlink = models.TextField(verbose_name="Hyperlink")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.copyright

   class Meta:
       verbose_name = "Base Text Field Copyright"
       verbose_name_plural = "Base Text Field Copyright"


class ShowcaseBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Showcase Background Image"
       verbose_name_plural = "Showcase Background Images"


class BilletBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Billet Background Image"
       verbose_name_plural = "Billet Background Images"


class BlogBackgroundImage(models.Model):
   title = models.TextField(verbose_name="Title")
   cover = models.ImageField(upload_to='images/', verbose_name="Cover")

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Blog Background Image"
       verbose_name_plural = "Blog Background Images"


class PostBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   # name = models.CharField(max_length=100, help_text='Your name goes here.')
   # description = models.TextField(help_text='Idea your profile here.')
   # image = models.ImageField(help_text='Link a URL for your profile (scales to your picture`s dimensions.)')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Idea Background Image"
       verbose_name_plural = "Idea Background Images"


class PosteBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   # name = models.CharField(max_length=100, help_text='Your name goes here.')
   # description = models.TextField(help_text='Idea your profile here.')
   # image = models.ImageField(help_text='Link a URL for your profile (scales to your picture`s dimensions.)')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Idea Background Image"
       verbose_name_plural = "Idea Background Images"


class VoteBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   # name = models.CharField(max_length=100, help_text='Your name goes here.')
   # description = models.TextField(help_text='Idea your profile here.')
   # image = models.ImageField(help_text='Link a URL for your profile (scales to your picture`s dimensions.)')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Vote Background Image"
       verbose_name_plural = "Vote Background Images"


class RuleBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Rule Background Image"
       verbose_name_plural = "Rule Background Images"


class AboutBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "About Background Image"
       verbose_name_plural = "About Background Images"


class FaqBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "FAQ Background Image"
       verbose_name_plural = "FAQ Background Images"


class StaffBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Staff Background Image"
       verbose_name_plural = "Staff Background Images"


class StaffApplyBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Staff Application Background Image"
       verbose_name_plural = "Staff Application Background Images"


class InformationBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Information Background Image"
       verbose_name_plural = "Information Background Images"


class TagBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Tag Background Image"
       verbose_name_plural = "Tag Background Images"


class UserBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "User Background Image"
       verbose_name_plural = "Users Background Images"


class StaffRanksBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Staff Ranks Background Image"
       verbose_name_plural = "Staff Ranks Background Images"


class MegaBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Mega Background Image"
       verbose_name_plural = "Mega Background Images"


# megacoins.html


class EventBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Event Background Image"
       verbose_name_plural = "Event Background Images"


class NewsBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "News Background Image"
       verbose_name_plural = "News Background Images"


class ShareBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Share Background Image"
       verbose_name_plural = "Share Background Images"


class WhyBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Why Background Image"
       verbose_name_plural = "Why Background Images"


class WebsiteBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Website Background Image"
       verbose_name_plural = "Website Background Images"


class PerksBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Perks Background Image"
       verbose_name_plural = "Perks Background Images"


class CommitmentBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Commitment Background Image"
       verbose_name_plural = "Commitment Background Images"


class PriceBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Price Background Image"
       verbose_name_plural = "Price Background Images"


class ServerBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Server Background Image"
       verbose_name_plural = "Server Background Images"


class ContactBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Contact Background Image"
       verbose_name_plural = "Contact Background Images"


class MantenienceBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Mantenience Background Image"
       verbose_name_plural = "Mantenience Background Images"


class CostBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Cost Background Image"
       verbose_name_plural = "Cost Background Images"


class TiersBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Tiers Background Image"
       verbose_name_plural = "Tiers Background Images"


class AccountBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Account Background Image"
       verbose_name_plural = "Account Background Images"


class AddonsBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Addons Background Image"
       verbose_name_plural = "Addons Background Images"


class PunishAppsBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Punishment Applications Background Image"
       verbose_name_plural = "Punishment Applications Background Images"


class BanAppealBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Ban Appliciations Background Image"
       verbose_name_plural = "Ban Applications Background Images"


# class Background2aImage(models.Model):
#  image = models.URLField(help_text='Upload a background image for the Introduction Section (section 2a).')

#  def get_absolute_url(self):
#    return self.image

#  class Meta:
#    verbose_name = "Background Image"
#    verbose_name_plural = "Background Images"

# class Background2aImage(models.Model):
#  image = models.URLField(help_text='Upload a background image for the Introduction Section (section 2a).')

#  def get_absolute_url(self):
#    return self.image

#  class Meta:
#    verbose_name = "Background Image"
#    verbose_name_plural = "Background Images"

from django.db.models.signals import post_save

# class PublicProfile(models.Model):
# user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
# photo = models.ImageField(verbose_name=("Profile Picture"),
#                  upload_to = 'profiles', #"main.PublicProfile.photo"
#                  format="Image", max_length=255, null=True, blank=True)
# website = models.URLField(default='', blank=True)
# username = models.CharField(max_length=100)
# bio = models.TextField(default='', blank=True)
# phone = models.CharField(max_length=20, blank=True, default='')
# city = models.CharField(max_length=100, default='', blank=True)
# country = models.CharField(max_length=100, default='', blank=True)
# organization = models.CharField(max_length=100, default='', blank=True)

# def create_profile(sender, **kwargs):
# user = kwargs["instance"]
# if kwargs["created"]:
# user_profile = UserProfile(user=user, bio='my bio') #website='http://poketrove.com')
# user_profile.save()
# post_save.connect(create_profile, sender=User)
import random

from django.contrib.auth import get_user_model, get_user


class ProfileDetails(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   email = models.EmailField(blank=True, null=True)
   # username = models.OneToOneField(User, on_delete=models.CASCADE)
   avatar = models.ImageField(upload_to='profile_image', null=True, blank=True, verbose_name="Profile picture")
   alternate = models.TextField(verbose_name="Alternate text")
   about_me = models.TextField(blank=True, null=True)
   position = models.UUIDField(
       default=uuid.uuid4,
       editable=False,
       unique=True,
       help_text="Position for sorting",
   )
   # link_to_profile = models.URLField(default=1, blank=True, null=True, verbose_name="Link to profile") #possibly consider making this automatically fill with the link to the user's profile
   # consider making a randomized pk that is assigned to each invididual user and can be attached to the end of the default profile url like in this schema: "http://127.0.0.1:8000/profile/pk/
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return str(self.user)

   class Meta:
       verbose_name = "Account Profile"
       verbose_name_plural = "Account Profiles"


# link the profiledetails page to settings

from django.utils import timezone
import pytz
from django.utils.timezone import make_aware

from datetime import datetime


# Create your models here.
class Room(models.Model):
   name = models.CharField(max_length=1000)

   def get_absolute_url(self):
       # Construct the URL for the room detail page
       room_url = reverse("showcase:room", kwargs={'room': self.room})

       # Construct the query parameters
       final_url = f"{room_url}?username={self.signed_in_user.username}"

       return final_url


from urllib.parse import urlencode



class Message(models.Model):
   value = models.CharField(max_length=1000000)
   date = models.DateTimeField(default=timezone.now, blank=True)
   user = models.CharField(max_length=1000000, verbose_name="Username")
   signed_in_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='messages', verbose_name="User")
   room = models.CharField(max_length=1000000)
   image = models.ImageField(upload_to='images/', null=True, blank=True)
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")



   def save(self, *args, **kwargs):
       if not self.pk:
           # Get the associated ProfileDetails for the donor
           profile = ProfileDetails.objects.filter(user=self.signed_in_user).first()

           # Set the position to the position value from the associated ProfileDetails
           if profile:
               self.position = profile.position

       super().save(*args, **kwargs)

   def get_profile_url(self):
       profile = ProfileDetails.objects.filter(user=self.signed_in_user).first()
       if profile:
           return reverse('showcase:profile', args=[str(profile.pk)])


   def get_absolute_url(self):

       # Construct the URL for the room detail page
       room_url = reverse("showcase:room", kwargs={'room': str(self.room)})

       # Construct the query parameters
       final_url = f"{room_url}?username={self.signed_in_user.username}"

       return final_url

       """
   def _get_current_user(self):
       # Logic to retrieve the currently signed-in user
       # You can modify this according to your authentication mechanism
       return User.objects.get(username='example_user')

   def get_profile_url(self):
       return reverse('showcase:profile', args=[str(self.signed_in_user_id)])
   #def get_profile_url(self):
   #    return f"http://127.0.0.1:8000/profile/{self.signed_in_user_id}/"
"""


# is_active is new

# Create your models here.
class SupportChat(models.Model):
   name = models.CharField(max_length=1000)

   # datetime.now()
   # api_time = models.DateTimeField()


class SupportMessage(models.Model):
   value = models.CharField(max_length=1000000)
   # now = datetime.datetime.now()
   date = models.DateTimeField(default=timezone.now, blank=True)
   user = models.CharField(max_length=1000000)
   signed_in_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE,
                                      related_name='support_messages',
                                      verbose_name="User")

   room = models.CharField(max_length=1000000)  # newly added unique=True
   avatar = models.ImageField(upload_to='profile_image', null=True, blank=True)
   image = models.ImageField(upload_to='images/', null=True, blank=True)
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")


   def save(self, *args, **kwargs):
       if not self.pk:
           # Get the associated ProfileDetails for the donor
           profile = ProfileDetails.objects.filter(user=self.signed_in_user).first()
           # Set the position to the position value from the associated ProfileDetails
           if profile:
               self.position = profile.position

       super().save(*args, **kwargs)

   def get_profile_url(self):
       profile = ProfileDetails.objects.filter(user=self.signed_in_user).first()
       if profile:
           return reverse('showcase:profile', args=[str(profile.pk)])

   def get_absolute_url(self):
       # Construct the URL for the room detail page
       room_url = 'http://127.0.0.1:8000/supportchat/room'

       return room_url

   class Meta:
       verbose_name = "Support Message"
       verbose_name_plural = "Support Messages"

# is_active is new



class UserProfile(models.Model):
   user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
   # related name could be a possible solution
   one_click_purchasing = models.BooleanField(default=False)
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.user.username

   class Meta:
       verbose_name = "User Profile"
       verbose_name_plural = "User Profiles"


"""class Settings(models.Model):
 username = models.OneToOneField(User, on_delete=models.CASCADE)
 #password =
 full_name = models.CharField(max_length=200, blank=True, null=True)

 class Meta:
     verbose_name_plural = "Settings"
     """
from django.db.models.signals import pre_save


class Item(models.Model):
   title = models.CharField(max_length=100)
   price = models.FloatField()
   discount_price = models.FloatField(blank=True, null=True)
   category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
   label = models.CharField(choices=LABEL_CHOICES, max_length=1000)  # can use for cataloging products
   slug = models.SlugField()  # might change to automatically get the slug
   description = models.TextField()
   image = models.ImageField()
   # hyperlink = models.TextField(verbose_name = "Hyperlink", blank=True, null=True, help_text="Feedbacks will use this hyperlink as a link to this product.") #might change to automatically get the hyperlink by means of item filtering
   relateditems = models.ManyToManyField("self", blank=True, verbose_name="Related Items:")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Out of stock?")

   def __str__(self):
       return self.title

   def get_absolute_url(self):
       return reverse("showcase:product", kwargs={'slug': self.slug})

   def get_add_to_cart_url(self):
       return reverse("showcase:add-to-cart", kwargs={'slug': self.slug})

   def get_remove_from_cart_url(self):
       return reverse("showcase:remove-from-cart", kwargs={'slug': self.slug})

   def save(self, *args, **kwargs):
       if not self.slug:
           slug = self.slug

       super().save(*args, **kwargs)

   def get_profile_url(self):
       return reverse('showcase:product', args=[str(self.slug)])


class EBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')
   items = Item.objects.filter(is_active=1)
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.title

   # def __str__(self):
   #    return self.__annotations__title

   class Meta:
       verbose_name = "Ecommerce Background Image"
       verbose_name_plural = "Ecommerce Background Images"


from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib import messages


class ChatBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   # items = Item.objects.all()

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Chat Background Image"
       verbose_name_plural = "Chat Background Images"


class SupportChatBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   # items = Item.objects.all()

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Support Chat Background Image"
       verbose_name_plural = "Support Chat Background Images"


class PartnerBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Partner Background Image"
       verbose_name_plural = "Partner Background Images"


class ConvertBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Convert Background Image"
       verbose_name_plural = "Convert Background Images"


class ReasonsBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Reasons Background Image"
       verbose_name_plural = "Reasons Background Images"


class OrderBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Order Background Image"
       verbose_name_plural = "Order Background Images"


class CheckoutBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Checkout Background Image"
       verbose_name_plural = "Checkout Background Images"


class SignupBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Signup Background Image"
       verbose_name_plural = "SignupBackground Images"


class ChangePasswordBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Change Password Background Image"
       verbose_name_plural = "Change Password Background Images"


class IssueBackgroundImage(models.Model):
   title = models.TextField()
   cover = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = "Issue Background Image"
       verbose_name_plural = "Issue Background Images"


class OrderItem(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   ordered = models.BooleanField(default=False)
   # order = models.ForeignKey(Order, on_delete=models.CASCADE)
   # order_number = models.IntegerField()
   slug = models.SlugField(max_length=200, blank=True, null=True,
                           help_text="Leave blank to use corresponding product slug.")  # apply unique=True parameter after slugs are actually implemented
   item = models.ForeignKey(Item, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)
   # order_date = models.DateTimeField(auto_now_add=True, verbose_name="order date")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return f"{self.quantity} of {self.item.title}"

   def get_total_item_price(self):
       if self.item.discount_price:
           return self.quantity * self.get_discount_item_price()
       return self.quantity * self.item.price

   def get_discount_item_price(self):
       return self.quantity * self.item.discount_price

   def get_amount_saved(self):
       return self.get_total_item_price() - self.get_discount_item_price()

   def get_final_price(self):
       if self.item.discount_price:
           return self.get_discount_item_price()
       return self.get_total_item_price()

   def save(self, *args, **kwargs):
       super().save(*args, **kwargs)
       OrderItemField.objects.create(
           user=self.user,
           ordered=self.ordered,
           # order_number=self.order_number,
           slug=self.slug,
           item=self.item,
           orderitem_id=self,
           quantity=self.quantity,
           is_active=self.is_active,
       )

   class Meta:
       verbose_name_plural = 'Order Items'


""" def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.item.slug)
       super().save(*args, **kwargs)"""


class OrderItemField(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   ordered = models.BooleanField(default=False)
   # order_number = models.IntegerField()
   slug = models.SlugField(max_length=200, blank=True, null=True,
                           help_text="Leave blank to use corresponding product slug.")
   item = models.ForeignKey(Item, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)
   orderitem_id = models.ForeignKey(OrderItem, on_delete=models.CASCADE, verbose_name="Order item id", null=True)
   is_active = models.IntegerField(default=1, blank=True, null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return f"{self.quantity} of {self.item.title}"

   class Meta:
       verbose_name_plural = 'Order Item Fields'


class AdminRoles(models.Model):
   roles = models.CharField(max_length=30, verbose_name="Administration roles")
   role_description = models.TextField(verbose_name="Role Overview", blank='True', null='True')
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')),
                                   verbose_name="Is this role currently active?")

   def __str__(self):
       return self.roles

   class Meta:
       verbose_name_plural = 'Administrative Roles'


class AdminTasks(models.Model):
   task = models.CharField(max_length=30, verbose_name="Administration tasks")
   hyperlink = models.CharField(max_length=100, verbose_name="Task hyperlink", help_text='Only add if necessary',
                                blank='True', null='True')
   opennew = models.BooleanField(verbose_name="Open In New Tab?", default=False,
                                 choices=((True, 'Yes'), (False, 'No')),
                                 help_text="Please note all Administration Interface Pages should open in a new tab.")
   section = models.IntegerField(help_text='Position of the page link.', verbose_name='position')
   page_name = models.TextField(verbose_name="Page Name", blank="True", null="True")
   image = models.ImageField(verbose_name="Task image")
   alternate = models.TextField(verbose_name="Alternate text")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')),
                                   verbose_name="Is this task currently active?")

   def __str__(self):
       return self.task

   class Meta:
       verbose_name_plural = 'Administrative Tasks'


class AdminPages(models.Model):
   pages = models.CharField(max_length=30, verbose_name="Administration pages")
   hyperlink = models.CharField(max_length=100, verbose_name="Page hyperlinks")
   opennew = models.BooleanField(verbose_name="Open In New Tab?", default=False,
                                 choices=((True, 'Yes'), (False, 'No')),
                                 help_text="Please note all Administration Interface Pages should open in a new tab.")
   section = models.IntegerField(help_text='Position of the page link.',
                                 verbose_name='position')
   page_name = models.TextField(verbose_name="Page Name", blank="True", null="True")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active page?")

   def __str__(self):
       return self.pages

   class Meta:
       verbose_name_plural = 'Administrative Pages'


class Order(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   ref_code = models.CharField(max_length=20, blank=True, null=True)
   items = models.ManyToManyField(OrderItem)
   itemhistory = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Order history", null=True)
   feedback_url = models.URLField(blank=True)
   start_date = models.DateTimeField(auto_now_add=True)
   ordered_date = models.DateTimeField()
   ordered = models.BooleanField(default=False)
   shipping_address = models.ForeignKey('Address', related_name='shipping_address', on_delete=models.SET_NULL,
                                        blank=True, null=True)
   billing_address = models.ForeignKey('Address', related_name='billing_address', on_delete=models.SET_NULL,
                                       blank=True, null=True)
   payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
   coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)
   being_delivered = models.BooleanField(default=False)
   received = models.BooleanField(default=False)
   refund_requested = models.BooleanField(default=False)
   refund_granted = models.BooleanField(default=False)
   id = uuid4()
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active order?")
   '''
   1. Item added to cart
   2. Adding a billing address
   (Failed checkout)
   3. Payment
   (Preprocessing, processing, packaging etc.)
   4. Being delivered
   5. Received
   6. Refunds
   '''

   def __str__(self):
       return self.user.username

   def get_total_price(self):
       total = 0
       for order_item in self.items.all():
           total += order_item.get_final_price()
       if self.coupon:
           if self.coupon.percentDollars:
               total *= 1 - (0.01 * self.coupon.amount)
           else:
               total -= self.coupon.amount
       return total

       def get_profile_url(self):
           return reverse('showcase:profile', args=[str(self.slug)])


class Address(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   street_address = models.CharField(max_length=100)
   apartment_address = models.CharField(max_length=100)
   country = CountryField(multiple=False)
   zip = models.CharField(max_length=100)
   address_type = models.CharField(max_length=1000, choices=ADDRESS_CHOICES)
   default = models.BooleanField(default=False)
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active address?")

   def __str__(self):
       return self.user.username

   class Meta:
       verbose_name_plural = 'Addresses'


class Payment(models.Model):
   stripe_charge_id = models.CharField(max_length=50)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
   amount = models.FloatField()
   timestamp = models.DateTimeField(auto_now_add=True)
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return self.user.username


class Coupon(models.Model):
   code = models.CharField(max_length=150)
   amount = models.FloatField()
   percentDollars = models.BooleanField(default=False)
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active coupon?")

   def __str__(self):
       return self.code


class Refund(models.Model):
   order = models.ForeignKey(Order, on_delete=models.CASCADE)
   reason = models.TextField()
   accepted = models.BooleanField(default=False)
   email = models.EmailField()
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active refund?")

   def __str__(self):
       return f"{self.pk}"


def userprofile_receiver(sender, instance, created, *args, **kwargs):
   if created:
       userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)


class Contact(models.Model):
   name = models.TextField(help_text="Name")
   email = models.EmailField(max_length=200, verbose_name="Recipient of your message.")
   inquiry = models.CharField(max_length=100, help_text='Subject of your message.')
   message = models.TextField(help_text='Your message goes here.')

   class Meta:
       verbose_name = "Contact Message"
       verbose_name_plural = "Contact Messages"


class BusinessMailingContact(models.Model):
   name = models.TextField(help_text="Name")
   email = models.EmailField(max_length=200, verbose_name="Recipient of your message.")
   inquiry = models.CharField(max_length=100, help_text='Subject of your message.')
   message = models.TextField(help_text='Your message goes here.')

   class Meta:
       verbose_name = "Business Mailing Message"
       verbose_name_plural = "Business Mailing Messages"


class CheckoutAddress(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   street_address = models.CharField(max_length=100)
   apartment_address = models.CharField(max_length=100)
   country = CountryField(multiple=False)
   zip = models.CharField(max_length=100)
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Is this an active address?")

   def __str__(self):
       return self.user.username

   class Meta:
       verbose_name_plural = 'Checkout Addresses'


class ImageCarousel(models.Model):
   carouseltitle = models.CharField(max_length=100, help_text='Title of the image.', verbose_name="title")
   carouselcaption = models.TextField(help_text='Caption for the image.', verbose_name="caption")
   carouselimage = models.ImageField(help_text='Upload an image for the carousel.)',
                                     upload_to='images/', verbose_name='image')
   carouselposition = models.IntegerField(help_text='Positioning of the image within the carousel.',
                                          verbose_name='position')
   carouseltotal = models.IntegerField(help_text='Total number of images within the carousel.',
                                       verbose_name='total images')
   carouselpage = models.TextField(verbose_name="Page Name")
   hyperlink = models.TextField(verbose_name="Hyperlink")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   class Meta:
       verbose_name = "Image Carousel Idea"
       verbose_name_plural = "Image Carousel Posts"


from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile


class AdvertisementBase(models.Model):
   advertisementtitle = models.CharField(max_length=100, help_text='Advertisement title.',
                                         verbose_name="advertisement title")
   advertisement = models.ImageField(help_text='Image of the advertisement.', upload_to='images/',
                                     height_field="advertisement_width",
                                     width_field="advertisement_length")  # the variable usage of advertisement_width & advertisement_height prevent those fields from being edited
   advertisement_length = models.PositiveIntegerField(blank=True, null=True, default="100",
                                                      help_text='Original length of the advertisement (use for original ratio).',
                                                      verbose_name="advertisement length")
   advertisement_width = models.PositiveIntegerField(blank=True, null=True, default="100",
                                                     help_text='Original width of the advertisement (use for original ratio).',
                                                     verbose_name="advertisement width")
   length_for_resize = models.PositiveIntegerField(default=40, verbose_name="Resized Length")
   width_for_resize = models.PositiveIntegerField(default=600, verbose_name="Resized Width")
   advertisement_position = models.IntegerField(help_text='Positioning of the advertisement.', verbose_name='Position')
   page = models.TextField(verbose_name="Page Name")
   xposition = models.IntegerField(help_text='x-position.', verbose_name="x-position")
   yposition = models.IntegerField(help_text='x-position.', verbose_name="y-position")
   relevance = models.TextField(help_text='Relevance of advertisement')
   correlating_product = models.OneToOneField(Item, blank=True, null=True, on_delete=models.CASCADE)
   type = models.CharField(max_length=200, help_text='Type of product.')
   advertisement_hyperlink = models.TextField(verbose_name="Hyperlink")
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   class Meta:
       verbose_name = "Advertisement Base"
       verbose_name_plural = "Advertisement Base"

       def __unicode__(self):
           return self.advertisementtitle

   def save(self, *args, **kwargs):
       if not self.id:  # object is being created for the first time
           super().save(*args, **kwargs)
           img = Image.open(self.advertisement.path)
           img = img.resize((self.width_for_resize, self.length_for_resize), Image.ANTIALIAS)
           self.advertisement_length, self.advertisement_width = img.size
           super().save(*args, **kwargs)
       else:  # object already exists and is being updated
           img = Image.open(self.advertisement.path)
           img = img.resize((self.width_for_resize, self.length_for_resize), Image.ANTIALIAS)
           self.advertisement_width, self.advertisement_length = img.size
           super().save(*args, **kwargs)


class Advertising(AdvertisementBase):
   pass


class ImageBase(models.Model):
   title = models.CharField(max_length=100, help_text='Advertisement title.',
                            verbose_name="advertisement title")
   image = models.ImageField(help_text='Image of the advertisement.', upload_to='images/',
                             height_field="image_length",
                             width_field="image_width")  # the variable usage of advertisement_width & advertisement_height prevent those fields from being edited
   image_width = models.PositiveIntegerField(blank=True, null=True, default="100",
                                             help_text='Width of the image (in percent relative).',
                                             verbose_name="image width")
   image_length = models.PositiveIntegerField(blank=True, null=True, default="100",
                                              help_text='Length of the image (in percent relative).',
                                              verbose_name="image length")
   width_for_resize = models.PositiveIntegerField(default=600, verbose_name="Resize Width")
   height_for_resize = models.PositiveIntegerField(default=40, verbose_name="Resize Height")
   image_position = models.IntegerField(help_text='Positioning of the image.', verbose_name='Position')
   alternate = models.TextField(verbose_name="Alternate Text")
   page = models.TextField(verbose_name="Page Name")
   xposition = models.IntegerField(help_text='x-position.', verbose_name="x-position", default="0")
   yposition = models.IntegerField(help_text='x-position.', verbose_name="y-position", default="0")
   relevance = models.TextField(help_text='Relevance of advertisement')
   correlating_product = models.OneToOneField(Item, blank=True, null=True, on_delete=models.CASCADE)
   # try incorporating other models in addition to Item
   type = models.CharField(max_length=200, help_text='Type of image.')
   hyperlink = models.TextField(verbose_name="Hyperlink", blank=True, null=True)
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   class Meta:
       # Add verbose name
       verbose_name = 'Image Base'
       verbose_name_plural = 'Image Base'

   def image_save(self, *args, **kwargs):
       if not self.id:  # object is being created for the first time
           super().save(*args, **kwargs)
           img = Image.open(self.image.path)
           img = img.resize((self.width_for_resize, self.height_for_resize), Image.ANTIALIAS)
           self.image_length, self.image_width = img.size
           super().save(*args, **kwargs)
       else:  # object already exists and is being updated
           img = Image.open(self.advertisement.path)
           img = img.resize((self.width_for_resize, self.height_for_resize), Image.ANTIALIAS)
           self.image_width, self.image_length = img.size
           super().save(*args, **kwargs)

   def set_image_position(image_id, xposition, yposition):
       # Retrieve the Image object from the database
       image = ImageBase.objects.get(id=image_id)
       print("Current coordinates: x={image.x}, y={image.y}")

       # Set the x and y positions to the desired values
       image.x = xposition
       image.y = yposition

       # Save the updated Image object back to the database
       image.save()


from django.utils import timezone


class State(models.Model):
   name = models.CharField(max_length=50)
   is_active = models.IntegerField(default=1, blank=True, null=True, help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")
   created_on = models.DateTimeField(default=timezone.now)
   updated_on = models.DateTimeField(default=timezone.now,
                                     null=True,
                                     blank=True)

   def __str__(self):
       return self.name

   class Meta:
       db_table = 'state'
       # Add verbose name
       verbose_name = 'Website'


class UserProfile2(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   first_name = models.CharField(max_length=100, default='')
   last_name = models.CharField(max_length=100, default='')
   description = models.CharField(max_length=100, default='')
   city = models.CharField(max_length=100, default='')
   country = models.CharField(max_length=100, default='')
   phone = models.IntegerField(default=0)
   profile_picture = models.ImageField(upload_to='profile_image', null=True, blank=True)

   class Meta:
       verbose_name = "Edit Profile"
       verbose_name_plural = "Edit Profiles"


def create_profile(sender, **kwargs):
   if (kwargs['created']):
       user_profile = UserProfile2.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class Feedback(models.Model):
   item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True,
                            null=True)  # might want to replace item with order
   # orderitem = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)  # might want to replace item with order
   order = models.ForeignKey(OrderItem, on_delete=models.CASCADE, blank=True, null=True)
   # order = models.OneToOneField(OrderItem, on_delete=models.CASCADE, related_name='feedback', null=True)
   username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
   hyperlink = models.CharField(max_length=200,
                                help_text="Leave field blank, hyperlink will automatically fill with the link to the associated product.")
   comment = models.TextField()
   feedbackpage = models.TextField(verbose_name="Page Name", blank=True, null=True)
   slug = models.SlugField(max_length=200,
                           help_text="Leave blank to use corresponding product slug.")  # get the actual item slug
   # unique=True prevents saving, but does not prevent the IntegrityError at /create_review/1/ UNIQUE constraint failed: showcase_feedback.slug
   star_rating = models.IntegerField(verbose_name='Star Rating',
                                     validators=[MinValueValidator(1), MaxValueValidator(5)])
   timestamp = models.DateTimeField(default=timezone.now)
   is_active = models.IntegerField(default=1,
                                   blank=True,
                                   null=True,
                                   help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')), verbose_name="Set active?")

   def __str__(self):
       return "%s %s" % (self.username, self.item)

   def get_current_username(self):
       User = get_user_model()
       return User.objects.get(pk=self.request.user.pk).username


@receiver(pre_save, sender=Feedback)
def set_slug(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = instance.item.slug

