'use strict';

var gulp = require('gulp'),
    sass = require('gulp-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    del = require('del'),
    browserSync = require('browser-sync'),
    path = require('path'),
    exec = require('child_process').exec,
    reload = browserSync.reload;

gulp.task('styles', function() {
  gulp.src('src/*.scss')
      .pipe(sass({
        includePaths: [
          path.join(__dirname, '/node_modules/bootstrap/scss/'),
        ]
      }).on('error', sass.logError))
      .pipe(autoprefixer({
        browsers: ['last 2 versions'],
        cascade: false
      }))
      .pipe(gulp.dest('files/'))
      .pipe(reload({ stream: true }));
});

gulp.task('assets', function() {
  gulp.src(['src/*.html', 'src/*.pdf', 'src/*.js'])
      .pipe(gulp.dest('files/'))
      .pipe(reload({ stream: true }));
});
gulp.task('nikola-build', function(cb) {
  exec('nikola build', function (err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
    cb(err);
  });
});

gulp.task('nikola-clean', function(cb) {
  exec('nikola clean', function (err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
    cb(err);
  });
});

gulp.task('build', ['styles', 'assets', 'nikola-build']);

gulp.task('clean', function() {
  del(['files/**']);
});

gulp.task('start', ['clean', 'build'], function() {
  browserSync({
    server: {
      baseDir: 'output/'
    }
  });

  gulp.watch('src/style.scss', ['styles']);
  gulp.watch(['**/*.rst', '**/*.html', '**/*.tmpl'], ['nikola-build']);
});

gulp.task('default', ['build']);
