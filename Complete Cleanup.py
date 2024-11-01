"""
BSD 2-Clause License

Copyright (c) [2021], [Shuai Xu]
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Shuai Xu  date:2020/12/15  time:20:47
#         School Of Life Sciences, Tsinghua University
#         Beijing Advanced Innovation Center For Structural Biology

from bluelake import fluidics, pause

STEP = 1


def single_step(pressure=1.5, minutes=10):
    print("Turn on selected valves...")
    fluidics.open(1, 2, 3, 4, 6)
    print("Valves are turned on successfully.")
    pause(1)

    # Increase Pressure
    while fluidics.pressure < pressure:
        fluidics.increase_pressure()
        print(f"Current pressure:{fluidics.pressure:.2f} < {pressure:.2f}, increasing pressure.")
        pause(0.1)
    while fluidics.pressure > pressure + 0.1:
        print(f"Current pressure:{fluidics.pressure:.2f} > {pressure + 0.1:.2f}, decreasing pressure.")
        fluidics.decrease_pressure()
        pause(0.1)
    print('Pressure is well!')
    print(f"Start to clean, total time = {minutes:d} minutes.")
    for i in range(minutes):
        pause(60)
        print(f"Elapsed minutes:{i + 1:d}, total minutes:{minutes:d}")
    fluidics.stop_flow()


if STEP == 1:
    print("----------Step 1: H2O----------")
    single_step(minutes=20)
    print("----------Step 1 is over----------")
elif STEP == 2:
    print("----------Step 2: Bleach----------")
    single_step(pressure=1, minutes=6)
    single_step(pressure=0.5, minutes=26)
    print("----------Step 2 is over----------")
elif STEP == 3:
    print("----------Step 3: H2O----------")
    single_step(minutes=6)
    print("----------Step 3 is over----------")
elif STEP == 4:
    print("----------Step 4: HCl----------")
    single_step()
    print("----------Step 4 is over----------")
elif STEP == 5:
    print("----------Step 5: H20----------")
    single_step()
    print("----------Step 5 is over----------")
elif STEP == 6:
    print("----------Step 6: Na2S2O3----------")
    single_step()
    print("----------Step 6 is over----------")
elif STEP == 7:
    print("----------Step 7: H2O----------")
    single_step(minutes=20)
    print("----------Step 7 is over----------")
