import java.util.Vector;

/**
 * Class that represents a sample. this is for JES, and
 * beware arrays are 1-index..?
 * Copyright Georgia Institute of Technology 2006
 * @author Timmy Douglas timmy@cc
 */
public class Samples
{  

  /**
   * the sound we point to
   */
    private Sound sound = null;

  /**
   * A collection of the threads that are playing this sound.
   */
    private Sample[] samples;

  
  
  /**
   * Constructor that takes a file name
   * @param aSound the name of the file to read the sound from
   */
    public Samples(Sound aSound)
    {
        this.sound = aSound;
        this.samples = new Sample[aSound.getLength()];
        for (int i=0; i < aSound.getLength(); i++) {
            samples[i] = new Sample(aSound, i);
        }
    }
  

  /**
   * @param aSound the name of the file to read the sound from
   * @return samples
   */
    static public Sample[] getSamples(Sound aSound)
    {
        Sample[] samples = new Sample[aSound.getLength()];
        for (int i=0; i < aSound.getLength(); i++) {
            samples[i] = new Sample(aSound, i);
        }
        return samples;
    }
  


  /**
   * Obtains a string representation of this JavaSound. 
   * @return a String representation of this JavaSound.
   */

  public String toString()
  {
      return ("Samples, length " + this.sound.getLength());
  }

  /**
   * gets item
   * @param index the index to get the sample
   * @return a sample
   */

  public Sample getSample(int index)
  {
      return this.samples[index];
  }


    /**
     * sets item
     * @param index the index to get the sample
     * @param value the value to set it to
     */
    
    
    public void setSample(int index, int value) throws SoundException
    {
        this.samples[index].setValue(value);
    }


    /**
     * sets item
     * @param index the index to get the sample
     * @param value the value to set it to
     */
    

    
    public void setSample(int index, double value) throws SoundException
    {
        this.setSample(index, Math.round(value));
    }


  /**
   * get sound object
   * @return a sound object
   */

  public Sound getSound()
  {
      return this.sound;
  }



}
