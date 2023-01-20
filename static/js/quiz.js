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
                // console.log(course.slug)
                options += `<option value="/quiz/quiz/${course.slug}/">${course.name}</option>`
            });
            console.log(courses)
            $('.courses-list').html(`
                <select class="custom-select courses-select" onchange="window.location=this.value"id="inputGroupSelect01">
                    <option disabled selected>COURSES</option>
                    ${options}
                </select>
            `)
        }
    })
    console.log(optionValue)
})


