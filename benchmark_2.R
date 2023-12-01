# Get a speed profile
#
# Usage:
#
# Rscript benchmark_2.R
#
library(profvis)
source("benchmark_2_code.R")
profvis(do_complex_calculation(size = 5))

