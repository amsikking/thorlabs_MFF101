import thorlabs_MFF101

# make 'instance' of device from 'class':
flipper = thorlabs_MFF101.Controller(
    'COM5',                 # pick the correct COM port
    name='MFF101',          # optional change name
    verbose=True,           # optional verbose
    very_verbose=False      # optional very_verbose
    )

# call whatever:
flipper.get_position()
flipper.flip(2)
flipper.flip(1)

# close
flipper.close()
