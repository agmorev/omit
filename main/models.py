from django.db import models
from django.utils.translation import gettext_lazy as _


class PortfolioItem(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=10, choices=(('0', _("web")), ('1', _("app"))), null=True, blank=True)
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    project_date = models.DateField(null=True, blank=True)
    project_url = models.URLField(null=True, blank=True)
    client = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = _('Portfolio item')
        verbose_name_plural = _('Portfolio items')
        ordering = ('name',)
    
    def __str__(self):
        return self.name


class PortfolioItemGallery(models.Model):
    item = models.ForeignKey(PortfolioItem, on_delete=models.CASCADE, related_name='portfolio_item')
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)

    class Meta:
        verbose_name = _('Portfolio item gallery')
        verbose_name_plural = _('Portfolio item gallery')
        ordering = ('name',)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return str(self.item)


class ServiceItem(models.Model):
    COLOR_CHOICES = (
        ('blue', 'Blue'),
        ('orange', 'Orange'),
        ('pink', 'Pink'),
        ('yellow', 'Yellow'),
        ('red', 'Red'),
        ('teal', 'Teal'),
    )

    DELAY_CHOICES = (
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
        ('500', '500'),
        ('600', '600'),
    )

    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Name of the service"),
    )
    image = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Presentation icon of the service (for example, 'bx bxl-dribbble')"),
    )
    color = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=COLOR_CHOICES,
        default="blue",
        help_text=_("Background 'on hover' color of the service icon"),
    )
    svg_path = models.TextField(
        null=True,
        blank=True,
        help_text=_("SVG path <d> attribute"),
    )
    data_aos_delay = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=DELAY_CHOICES,
        default="blue",
        help_text=_("Background 'on hover' color of the service icon"),
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_("Description of the service. HTML tags can be used for text format"),
    )
    full_description = models.TextField(
        null=True,
        blank=True,
        help_text=_("Full description of the service. HTML tags can be used for text format"),
    )

    class Meta:
        verbose_name = _('Service item')
        verbose_name_plural = _('Service items')
        ordering = ('name',)

    def __str__(self):
        return self.name


class ServiceItemGallery(models.Model):
    item = models.ForeignKey(
        ServiceItem,
        on_delete=models.CASCADE,
        related_name='service_item',
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Name of the service details slider image"),
    )
    image = models.ImageField(
        upload_to='services/items/',
        null=True,
        blank=True,
        help_text=_("Image of the service details slider"),
    )

    class Meta:
        verbose_name = _('Service item gallery')
        verbose_name_plural = _('Service item gallery')
        ordering = ('name',)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return str(self.item)


class ServiceItemClients(models.Model):
    item = models.ForeignKey(
        ServiceItem,
        on_delete=models.CASCADE,
        related_name='service_client',
    )
    name = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        help_text=_("Name of the client"),
    )
    image = models.ImageField(
        upload_to='services/clients/',
        null=True,
        blank=True,
        help_text=_("Logo image of the client"),
    )

    class Meta:
        verbose_name = _('Service item client')
        verbose_name_plural = _('Service item clients')
        ordering = ('name',)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return str(self.item)