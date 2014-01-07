"""

"""

from framework import fields
from website.addons.base import AddonSettingsBase


class AddonFigShareSettings(AddonSettingsBase):

    figshare_id = fields.StringField()

    @property
    def embed_url(self):
        return 'http://wl.figshare.com/articles/{fid}/embed?show_title=1'.format(
            fid=self.figshare_id,
        )

    def to_json(self):
        return {
            'figshare_id': self.figshare_id,
        }
