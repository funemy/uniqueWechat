$(document).ready(function(){
    $("button.btn-pass").on("click",function(){
        var $this = $(this);
        $.ajax({
            method: "put",
            url: "/invite/" + $(this).data("tid") + "/1"
        }).success(function(){
            $this.parent().html("已确认");
        });
    });
    $("button.btn-refuse").on("click",function(){
        var $this = $(this);
        $.ajax({
            method: "put",
            url: "/invite/" + $(this).data("tid") + "/0"
        }).success(function(){
            $this.parent().html("已确认");
        });
    });
    $('#myModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);// Button that triggered the modal
        var tid = button.data('tid');// Extract info from data-* attributes
        console.log(tid);
        //// If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        //// Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        var modal = $(this);
        modal.find('#item-id').val(tid);
        //modal.find('.modal-body input').val(recipient)
    });
    $('#time_submit').on('click', function(){
        $.ajax({
            method: "put",
            url: "/info?" + $('#form_time').serialize()
        }).success(function(){
            $("#myModal").modal('hide');
        });
    });
});