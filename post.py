# To post, create an actual API instance.

from mastodon import Mastodon

mastodon = Mastodon(access_token = 'pytooter_usercred.secret')
mastodon.toot('Tooting from Python using #mastodonpy !')