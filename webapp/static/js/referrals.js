cr = cr || {};

cr.ReferralCollection = BB.Collection.extend({
    url: '/api/referrals/',
});

cr.ReferralsView = BB.View.extend({
    el: '#referrals',
    template: _.template($('#referrals-template').html()),
    modalTemplate: _.template($('#notes-modal-template').html()),
    notesTemplate: _.template($('#notes-table-template').html()),

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
        'click .add-referral': 'addReferral',
        'click .notes-opener': 'openNotesModal',
        'click .add-note': 'addNote'
    },

    addReferral: function (e) {
        var name = this.$('.client-name-input').val(),
            org = this.$('.org-chooser').val();

        this.outgoingCollection.add({
            id: 1,
            client_name: name,
            date_referred: '5/2/2017',
            referring_entity: 'Shelter #1',
            referring_to: org,
            referral_status: 'arrived',
            notes: []
        });

        this.render();
    },

    openNotesModal: function (e) {
        var refId = parseInt($(e.target).attr('data-id')),
            section = $(e.target).attr('data-section');

        if (section === 'incoming') {
            var refData = _.findWhere(this.incomingCollection.toJSON(), {id: refId});
        } else {
            var refData = _.findWhere(this.outgoingCollection.toJSON(), {id: refId});
        }

        this.$('.modal-holder').empty().append(this.modalTemplate(_.extend(refData, {section: section})));
        this.$('.notes-row').empty().append(this.notesTemplate(_.extend(refData, {section: section})));
        this.$('#notes-modal').openModal();
    },

    addNote: function (e) {
        var text = this.$('.add-note-input').val(),
            refId = parseInt($(e.target).attr('data-id')),
            section = $(e.target).attr('data-section');

        if (section === 'incoming') {
            var refData = _.findWhere(this.incomingCollection.toJSON(), {id: refId});
        } else {
            var refData = _.findWhere(this.outgoingCollection.toJSON(), {id: refId});
        }

        refData.notes.push({author: 'Drew Winship', text: text, date: '5/2/2017'});
        this.$('.notes-row').empty().append(this.notesTemplate(_.extend(refData, {section: section})));
    },
});
