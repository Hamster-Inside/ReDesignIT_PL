$(document).ready(function() {
    $("#login-as-test-user").click(function() {
        $("#id_email").val("TestUser.ReDesignIT@gmail.com");
        $("#id_password").val("Mandarynki45$45");
        $("#login-form").submit();
    });
    $("#id_email").val("")
});