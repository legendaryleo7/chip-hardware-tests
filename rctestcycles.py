import rotary_encoder

A_PIN = "XIO-P0"
B_PIN = "XIO-P1"

encoder = rotary_encoder.RotaryEncoder.Worker(A_PIN, B_PIN)
encoder.start()


while 1:
    delta = encoder.get_cycles()
    if delta != 0:
        print "rotated %d cycles" % delta

except KeyboardInterrupt:
    import CHIP_IO.Utilities as UT
    UT.unexport_all()
