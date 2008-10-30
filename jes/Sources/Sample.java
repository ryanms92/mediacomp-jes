
/**
 * Class that represents a sample. this is for JES, and
 * arrays are 1-index
 * Copyright Georgia Institute of Technology 2006
 * @author Timmy Douglas timmy@cc
 */
public class Sample
{

  /**
   * the sound we point to
   */
    private Sound sound = null;

  /**
   * the sample index
   */
    private int index;



  /**
   * Constructor that takes a file name
   * @param aSound the sound
   * @param index the index
   */
    public Sample(Sound aSound, int index) {
        this.index = index;
        this.sound = aSound;
    }

  /**
   * Obtains a string representation of this JavaSound.
   * @return a String representation of this JavaSound.
   */

  public String toString()
  {
      try {
          return ("Sample at " + (this.index + SimpleSound._SoundIndexOffset) + " with value " + this.getValue());
      } catch (Exception e) {
          return ("Sample at " + (this.index + SimpleSound._SoundIndexOffset) + " value unknown");

      }
  }

  /**
   * get sound object
   * @return a sound object
   */

  public Sound getSound()
  {
      return this.sound;
  }


  /**
   * get sample value
   * @return a sample value
   */

  public int getValue() throws SoundException
  {
      return this.sound.getSampleValueAt(this.index);
  }


  /**
   * get sample value
   * @param newValue the new value to store
   */

  public void setValue(int newValue) throws SoundException
  {
      // System.out.println("setValue!!");
      this.sound.setSampleValueAt(this.index, newValue);
  }


  /**
   * get sample value
   * @param newValue the new value to store
   */

  public void setValue(double newValue) throws SoundException
  {
      this.setValue((int)newValue);
  }

}
