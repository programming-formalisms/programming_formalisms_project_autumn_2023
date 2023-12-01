
# Determines if data is sorted
is_sorted <- function(data) {
  all(data == sort(data))
}

testthat::expect_true(is_sorted(c(1,2,3)))
testthat::expect_false(is_sorted(c(2,1,3)))

# Sorts data by Richelsort
richel_sort <- function(data) {
  while (!is_sorted(data)) {
    data <- sample(1:length(data))
  }
  data
}

testthat::expect_true(is_sorted(richel_sort(c(1,2,3))))
testthat::expect_true(is_sorted(richel_sort(c(2,1,3))))
testthat::expect_true(is_sorted(richel_sort(c(3,2,1))))

# Create the data to be sorted
create <- function(size = 10) {
  testthat::expect_true(size > 0)
  seq(0, size)
}

# Reverse the list
reverse <- function(x) {
  rev(x) 
}

testthat::expect_equal(reverse(c(1, 2)), c(2,1))

# Sort the list
do_sort <- function(x) {
  richel_sort(x)
}

testthat::expect_true(is_sorted(do_sort(c(1,2,3))))
testthat::expect_true(is_sorted(do_sort(c(2,1,3))))
testthat::expect_true(is_sorted(do_sort(c(3,2,1))))

# Does a complex calculation.
#
# Vague wording is intentional.
do_complex_calculation <- function(size = 10) {
  do_sort(reverse(create(size = size)))
}

profvis::profvis(do_complex_calculation(size = 7))
