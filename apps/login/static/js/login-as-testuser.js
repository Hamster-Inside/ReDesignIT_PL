$(document).ready(function() {
    $("#login-as-test-user").click(function() {
        $("#id_email").val("Test@ReDesignIT.pl");
        $("#id_password").val("JustARandomBox$85");
        $("#test-user-action").val("register");
        $("#login-form").submit();
    });
    $("#id_email").val("");
});