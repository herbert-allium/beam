#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# beam-playground:
#   name: CompositeTransform
#   description: Task from katas to implement a composite transform "ExtractAndMultiplyNumbers"
#     that extracts numbers from comma separated line and then multiplies each number by 10.
#   multifile: false
#   context_line: 31
#   categories:
#     - Flatten
#   complexity: BASIC
#   tags:
#     - count
#     - strings
#     - numbers

import apache_beam as beam

from log_elements import LogElements


class ExtractAndMultiplyNumbers(beam.PTransform):

    def expand(self, pcoll):
        return (pcoll
                | beam.FlatMap(lambda line: map(int, line.split(',')))
                | beam.Map(lambda num: num * 10)
                )


with beam.Pipeline() as p:

  (p | beam.Create(['1,2,3,4,5', '6,7,8,9,10'])
     | ExtractAndMultiplyNumbers()
     | LogElements())
