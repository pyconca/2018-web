'use strict';

var gulp = require('gulp'),
    sass = require('gulp-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    del = require('del'),
    browserSync = require('browser-sync'),
    reload = browserSync.reload;

gulp.task('styles', function() {
  gulp.src('src/*.scss')
      .pipe(sass().on('error', sass.logError))
      .pipe(autoprefixer({
        browsers: ['last 2 versions'],
        cascade: false
      }))
      .pipe(gulp.dest('build/'))
      .pipe(reload({ stream: true }));
});

gulp.task('assets', function() {
  gulp.src(['src/*.html', 'src/*.woff'])
      .pipe(gulp.dest('build/'))
      .pipe(reload({ stream: true }));
});

gulp.task('netlify-stuff', function() {
  gulp.src('_redirects')
      .pipe(gulp.dest('build/'))
      .pipe(reload({ stream: true }));
});

gulp.task('build', ['styles', 'assets', 'netlify-stuff']);

gulp.task('clean', function() {
  del(['build/**']);
});

gulp.task('start', ['clean', 'build'], function() {
  browserSync({
    server: {
      baseDir: 'build/'
    }
  });

  gulp.watch('src/**/*', ['build']);
});

gulp.task('default', ['build']);
