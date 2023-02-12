// For quizselect page
$('.levels-select').on('change', function(){
    var optionValue = $(this).val();
    $.ajax({
        type: 'POST',
        url: $(this).attr('data-url'),
        data: JSON.stringify({
            'levelValue': optionValue
        }),
        dataType: 'json',
        success: function(response){
            var courses = response.courses
            var options = ''
            courses.forEach((course) => {
                options += `<option value="/quiz/quiz/${course.slug}/">${course.name}</option>`
            });
            $('.courses-list').html(`
                <select class="custom-select courses-select" onchange="window.location=this.value" id="inputGroupSelect01">
                    <option disabled selected>COURSES</option>
                    ${options}
                </select>
            `)
        }
    })
})

$('#option-next-button').on('click', function(e){
    e.preventDefault();

    $('#option-value-form').submit()
    // const optionValue = $('input[name=option]:checked').val();

    // $.ajax({
    //     type: 'POST',
    //     url: '/quiz/quiz/',
    //     data: JSON.stringify({
    //         'option': optionValue,
    //     }),
    //     dataType: 'json',
    //     success: function(response){
    //         console.log(response.data);
    //     }
    // });

    // To send the Option Value
})