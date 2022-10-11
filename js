data = courses_arr.map(function(course) {
    x = {};
    x.description = course.getElementsByClassName("course_description")[0].innerHTML;
    x.name = course.children[0].name
    return x
})
