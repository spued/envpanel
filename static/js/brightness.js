$( document ).ready(function() {
     parse_brightness();
});
function parse_brightness() {
    if($("#brightness_value").val() != ''){
        let brightness = $("#brightness_value").val().split(",");
        //console.log(brightness);
        $("#select_morning_brightness").val(brightness[0]).trigger('change');
        $("#select_late_morning_brightness").val(brightness[1]).trigger('change');
        $("#select_afternoon_brightness").val(brightness[2]).trigger('change');
        $("#select_evening_brightness").val(brightness[3]).trigger('change');
        $("#select_night_brightness").val(brightness[4]).trigger('change');
    }
}

$("select").on("change",function(evt){
    let _brightness = $("#select_morning_brightness").val() + "," +
        $("#select_late_morning_brightness").val() + "," +
        $("#select_afternoon_brightness").val() + "," +
        $("#select_evening_brightness").val() + "," +
        $("#select_night_brightness").val();
    $("#brightness_value").val(_brightness);
})
/*
$(document).on("submit","#form_set_brightness", function(evt){
   evt.preventDefault();
   let _data = $("#brightness_value").val();
   console.log(_data);
});
*/
