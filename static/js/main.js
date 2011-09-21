(function(window, $) {
    var submit = $('form').find('.btn');
    submit.click(function(e){
        var form = $('form'),
            paragraphs = form.find('fieldset').find('input').val(),
            tags = form.find('select').val();

        e.preventDefault();

        $.ajax({
            url: '/generate',
            data: {
                paragraphs: paragraphs,
                tags: tags
            },
            success: function(data) {
                var textarea = $('textarea'),
                    paragraphs = data.paragraphs,
                    string = '';

                for (var i = 0; i < paragraphs.length; i++) {
                    string += paragraphs[i] + '\n\n';
                };

                textarea.val(string).focus();
            }
        });
    });
})(window, jQuery);
