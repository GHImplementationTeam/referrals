cr = {};
BB = Backbone;

_.templateSettings = {
    evaluate: /\{\{#(.+?)\}\}/g,
    interpolate: /\{\{=(.+?)\}\}/g,
    escape: /\{\{(?!#|=)(.+?)\}\}/g
};

cr.underscorePartial = function (templateSelector, data) {
    return _.template($('#' + templateSelector).html())(data);
};

cr.checkForEnter = function (e) {
    if (e.which == 13 && !e.shiftKey) {
        e.preventDefault();
        $(e.target).blur();
    }
};
