$("#addBtn").click(function() {

   if($("#nameText").val() == "") {
      alert("Please Enter college Name");
      $("#nameText").focus();
      return false;
   }
});
