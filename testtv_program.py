from tv_class import TV

def main():
    # Create two TV objects
    tv1 = TV()
    tv2 = TV()

    # Turn on TV1
    tv1.turn_on()
    # Set TV1 channel to 30
    tv1.set_channel(30)
    # Set TV1 volume level to 3
    tv1.set_volume(3)

    # Turn on TV2
    tv2.turn_on()
    # Set TV2 channel to 3
    tv2.set_channel(3)
    # Set TV2 volume level to 2
    tv2.set_volume(2)

    # Print the channel and volume of TV1
    print(f"tv1's channel is {tv1.channel} and volume level is {tv1.volume_level}")

    # Print the channel and volume of TV2
    print(f"tv2's channel is {tv2.channel} and volume level is {tv2.volume_level}")

# Call the main function if the script is executed directly.
if __name__ == "__main__":
    main()

