#!/usr/bin/env ruby
string = ARGV[0]
pattern = /\[from:([+\d\w]+)\] \[to:([+\d\w]+)\] \[flags:(.*?)\]/
matches = string.scan(pattern)

sender = matches[0][0]
receiver = matches[0][1]
flags = matches[0][2]

puts "#{sender},#{receiver},#{flags}"
