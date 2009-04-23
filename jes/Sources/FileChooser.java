import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.SwingWorker;
import java.util.Properties;
import java.io.*;
import java.net.*;

/**
 * A class to make working with a file chooser easier
 * for students.  It uses a JFileChooser to let the user
 * pick a file and returns the chosen file name.
 *
 * Copyright Georgia Institute of Technology 2004
 * @author Barb Ericson ericson@cc.gatech.edu
 */
public class FileChooser
{

  ///////////////////////////// class fields ///////////////////
   /**
   * Properties to use during execution
   */
  private static Properties appProperties = null;

  /**
   * Property key for the media directory
   */
  private static final String MEDIA_DIRECTORY = "mediaDirectory";

  /**
   * Name for property file
   */
  private static final String PROPERTY_FILE_NAME =
    "SimplePictureProperties.txt";

  private static JFileChooser fileChooser = null;

  private static String latestPath = null;

  /////////////////////// methods /////////////////////////////

  /**
   * Method to pick an item using the file chooser
   * @param fileChooser the file Chooser to use
   * @return the path name
   */
  public static String pickPath(JFileChooser fileChooser)
  {
    String path = null;

    /* create a JFrame to be the parent of the file
     * chooser open dialog if you don't do this then
     * you may not see the dialog.
     */
    JFrame frame = new JFrame();
    frame.setAlwaysOnTop(true);

    File latestFilePath = null;
    if ( latestPath != null )
    	latestFilePath = new File(latestPath);
   	if ( ( latestFilePath != null ) && ( latestFilePath.exists() ) )
   	{
		fileChooser.setCurrentDirectory( latestFilePath );
	}
	else
	{
		File file = new File( getMediaDirectory() );
		if ( file.exists() )
		{
			fileChooser.setCurrentDirectory( file );
		}
		else
		{
			fileChooser.setCurrentDirectory( new File( System.getProperty("user.home") ) );
		}
	}

    // get the return value from choosing a file
    int returnVal = fileChooser.showOpenDialog(frame);

    // if the return value says the user picked a file
    if (returnVal == JFileChooser.APPROVE_OPTION)
    {
      path = fileChooser.getSelectedFile().getPath();
      //update latestPath to the last path just picked
      latestPath = path;
    }

    return path;
  }

  /**
   * Method to let the user pick a file and return
   * the full file name as a string.  If the user didn't
   * pick a file then the file name will be null.
   * @return the full file name of the picked file or null
   */
  public static String pickAFile()
  {
    // start off the file name as null
    String fileName = null;

    // if no file chooser yet create one
//    if (fileChooser == null)
//      fileChooser = new JFileChooser();

    // allow files to be picked
    fileChooser.setFileSelectionMode(JFileChooser.FILES_ONLY);

    // pick the file
    fileName = pickPath(fileChooser);

    return fileName;
  }

  /**
   * Method to let the user pick a directory and return
   * the full path name as a string.
   * @return the full directory path
   */
  public static String pickADirectory()
  {
    String dirName = null;

    // if no file chooser yet create one
    if (fileChooser == null)
      fileChooser = new JFileChooser();

    // allow only directories to be picked
    fileChooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);

    // pick the directory
    dirName = pickPath(fileChooser);

    return dirName;
  }

   /**
  * Method to get the full path for the passed file name
  * @param fileName the name of a file
  * @return the full path for the file
  */
 public static String getMediaPath(String fileName)
 {
   String path = null;
   String directory = getMediaDirectory();

   // get the full path
   path = directory + fileName;

   return path;
 }

 /**
  * Method to get the directory for the media
  * @return the media directory
  */
 public static String getMediaDirectory()
 {
   return JESConfig.getMediaPath();
 }

 /**
  * Method to set the media path by setting the directory to use
  * @param directory the directory to use for the media path
  */
 public static void setMediaPath(String directory)
 {
   // check if the directory exists
   File file = null;
   if ( directory != null )
     file = new File( directory );
   if ( ( file == null ) || ( !file.exists() ) )
   {
     System.out.println("Sorry but " + directory +
                 " doesn't exist, try a different directory.");
   }
   else
   {
	 if ( !directory.endsWith( File.separator ) )
	 	directory += File.separator;
     JESConfig.setMediaPath( directory );
   }

 }

 /**
  * Method to pick a media path using
  * the file chooser and set it
  */
 public static void pickMediaPath()
 {
   String dir = pickADirectory();

   File file = null;
   if ( dir != null )
     file = new File( dir );
   if ( ( file == null ) || ( !file.exists() ) )
   {
     System.out.println("Sorry but " + dir +
                 " doesn't exist, try a different directory.");
   }
   else
   {
	 if ( dir == null )
	 	return;
	 if ( !dir.endsWith( File.separator ) )
	 	dir += File.separator;
     JESConfig.setMediaPath( dir );
   }
 }

 public static void loadFileChooser()
 {
	 try
	 {
		 //Try to load JFileChooser 5 times - each failed attempt increase wait time by 2 seconds.
		 for (int tries = 1; tries <= 5; tries++)
		 {
			 FileChooserLoader fcLoad = new FileChooserLoader();
			 //System.out.println("Loading JFileChooser, Attempt " + tries);
			 //System.out.println("Begin execution of Filechooserloader");
			 fcLoad.execute();
			 //System.out.println("Begin sleep 10000");
			 Thread.sleep( 2000*tries );
			 //System.out.println("Cancel Filechooserloader");
			 boolean cancelled = fcLoad.cancel( true );
			 //System.out.println( cancelled );
			 if ( cancelled )
			 	System.out.println("Filechooserloader attempt " + tries + " failed.");
			 else
			 {
			 	fileChooser = fcLoad.get();
			 	if ( fileChooser != null )
			 		break;
			 }
		 }
		 //System.out.println("JFileChooser tries completed");
	 }
	 catch (InterruptedException e)
	 {
		 //e.printStackTrace();
	 }
	 catch (java.util.concurrent.ExecutionException e)
	 {
		 //System.out.println("Execution exception");
		 //e.printStackTrace();
	 }
 }

 private static class FileChooserLoader extends SwingWorker<JFileChooser, Boolean>
 {
	 boolean fcLoaded = false;
	 public JFileChooser doInBackground()
	 {
		 try
		 {
			 //Thread.sleep( 9500 );
			 //Above for testing only
			 JFileChooser fc = new JFileChooser();
			 fcLoaded = true;
			 return fc;
		 }
		 catch(Exception e)
		 {
			 //System.out.println("Exception in doInBackground");
			 //e.printStackTrace();
			 return null;
		 }
	 }
	 /*
	 public void done()
	 {
		 if ( isLoaded() )
		 	System.out.println("JFileChooser loaded successfully!");
	 }
	 public boolean isLoaded()
	 {
		 return fcLoaded;
	 }
	 */
 }

}