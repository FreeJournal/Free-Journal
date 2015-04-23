var gulp = require('gulp');

var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');

gulp.task('sass', function () {
    gulp.src('./webapp/scss/*.scss')
        .pipe(sourcemaps.init())
        .pipe(sass())
        .on('error', handleError)
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('./webapp/public'));
});

gulp.task('watch', function() {
    gulp.watch('./webapp/scss/*.scss', ['sass']);
});

gulp.task('default', ['watch', 'sass']);

function handleError(error) {
    console.log("[ERROR] " + error.plugin + ": " + error.message);
}
