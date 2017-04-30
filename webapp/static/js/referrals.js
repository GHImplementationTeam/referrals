cr = cr || {};

cr.ReferralCollection = BB.Collection.extend({
    url: '/api/referrals/',
});

cr.ReferralsView = BB.View.extend({
    el: '#referrals',
    template: _.template($('#referrals-template').html()),
    modalTemplate: _.template($('#notes-modal-template').html()),

    initialize: function (options) {
        this.incomingCollection = new cr.ReferralCollection();
        this.outgoingCollection = new cr.ReferralCollection();

        this.listenTo(this.incomingCollection, 'sync', this.render);
        this.listenTo(this.outgoingCollection, 'sync', this.render);

        this.incomingCollection.fetch({
            data: {
                incoming: true
            },
        });

        this.outgoingCollection.fetch({
            data: {
                incoming: false
            },
        });

    },

    render: function () {
        if (this.incomingCollection.toJSON().length === 0 && this.outgoingCollection.toJSON().length === 0) {
            this.$el.empty().append('No data.');
        }

        this.$el.empty().append(this.template({
            incomingReferrals: this.incomingCollection.toJSON(),
            outgoingReferrals: this.outgoingCollection.toJSON(),
        }));
    },

    events: {
        'click .notes-opener': 'openNotesModal'
    },

    openNotesModal: function (e) {
        var refId = parseInt($(e.target).attr('data-id')),
            section = $(e.target).attr('data-section');

        if (section === 'incoming') {
            var refData = _.findWhere(this.incomingCollection.toJSON(), {id: refId});
        } else {
            var refData = _.findWhere(this.outgoingCollection.toJSON(), {id: refId});
        }

        this.$('.modal-holder').empty().append(this.modalTemplate(refData));
        this.$('#notes-modal').openModal();
    },
});
