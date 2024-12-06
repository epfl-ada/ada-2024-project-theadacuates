$(function () {
  //--------------------  Overlay --------------------

  // Open the overlay when a button is clicked
  $('button').click(function () {
    var overlayId = $(this).data('overlay-id')
    console.log(overlayId)
    if (overlayId !== undefined) {
      $(`div.overlay[data-overlay-id="${overlayId}"]`).removeClass('hidden')
    }
  })

  // Close the overlay when clicking outside the modal
  $(window).click(function (event) {
    if ($(event.target.matches('.overlay'))) {
      $(event.target).addClass('hidden')
    }
  })
})
