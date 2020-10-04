$(function() {


    // clone
    $('#btn-clone').click(function() {
        var text = $('.text').last();  // 最後尾にあるinput
        clone = text.clone().insertAfter(text);  // inputを最後尾に追加
        clone.find("input[type='text']").val('');  // valueもクローンされるので削除する
    });


    // ここからDjango用のidなどを操作する
    $('#form').submit(function() {  // フォームを送信する直前

        // フォームの入力欄の数を指定する
        const text = $('.text');
        $('[name=form-TOTAL_FORMS]').val(text.length);

        // それぞれの入力欄の__prefix__をindexで置換する
        text.each(function(index, element){
            html = $(element).html().replace(/__prefix__/g, index);
            value = $(element).find("input[type='text']").val();  // valueが消えるので保存しておく
            $(element).html(html);
            $(element).find("input[type='text']").val(value);
        });

    });
});