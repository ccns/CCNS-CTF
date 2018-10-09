from sqlalchemy.sql.expression import union_all
from marshmallow import fields, post_load
from marshmallow import validate, ValidationError
from marshmallow_sqlalchemy import field_for
from CTFd.models import ma, Hints


class HintSchema(ma.ModelSchema):
    class Meta:
        model = Hints
        dump_only = ('id',)

    views = {
        'user': [
            'id',
            'type',
            'challenge_id',
            'content',
            'cost'
        ],
        'admin': [
            'id',
            'type',
            'challenge_id',
            'content',
            'cost',
            'requirements'
        ]
    }

    def __init__(self, view=None, *args, **kwargs):
        if view:
            if type(view) == str:
                kwargs['only'] = self.views[view]
            elif type(view) == list:
                kwargs['only'] = view

        super(HintSchema, self).__init__(*args, **kwargs)