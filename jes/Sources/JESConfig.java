import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;

/**
 * The JES Config Class
 * Created for the Jython Environment for Students
 * The JESConfig Class reads the config file information for the JES
 * config file, located at JES_CONFIG_FILE_NAME
 */
public class JESConfig
{
	public static String JES_CONFIG_FILE_NAME = "JESConfig.txt";
	public static int CONFIG_NAME = 0;
	public static int CONFIG_GT = 1;
	public static int CONFIG_MAIL = 2;
	public static int CONFIG_MODE = 3;
	public static int CONFIG_FONT = 4;
	public static int CONFIG_EMAIL_ADDR = 5;
	public static int CONFIG_GUTTER = 6;
	public static int CONFIG_BLOCK = 7;
	public static int CONFIG_WEB_TURNIN = 8;
	public static int CONFIG_AUTOSAVEONRUN = 9;
	public static int CONFIG_AUTOOPENDOC = 10;
	public static int CONFIG_WRAPPIXELVALUES = 11;
	public static int CONFIG_SKIN = 12;
	public static int CONFIG_SHOWTURNIN = 13;
	public static int CONFIG_BACKUPSAVE = 14;
	public static int CONFIG_LOGBUFFER = 15;
	public static int CONFIG_MEDIAPATH = 16;
	public static int CONFIG_NLINES = 17;

	private ArrayList<String> properties;
	private String[] defaults = {"","","","Normal","12","","1","0","","0","","1","","0","1","1",""};
	private static boolean wrapAroundPixelValues;
	private static String mediaFolder;

	public static void main( String[] args )
	{
		JESConfig jConfig = new JESConfig();
		for( int i = 0; i < CONFIG_NLINES; i++ )
		{
			System.out.println( jConfig.getProperty( i ) );
		}
		System.out.println( JESConfig.wrapAroundPixelValues );
	}

	public JESConfig()
	{
		properties = readConfig();
		if ( properties == null )
		{
			properties = new ArrayList<String>( Arrays.asList( defaults ) );
		}
		JESConfig.wrapAroundPixelValues = ( 0 != Integer.parseInt( getProperty( CONFIG_WRAPPIXELVALUES ) ) );
		if (getProperty( CONFIG_MEDIAPATH ) == "" )
			setProperty( CONFIG_MEDIAPATH, System.getProperty("user.home") );
		JESConfig.mediaFolder = getProperty( CONFIG_MEDIAPATH );
	}

	public ArrayList<String> getProperties()
	{
		return properties;
	}

	public String getProperty( int property )
	{
		if ( ( property >= 0 ) && ( property < CONFIG_NLINES ) )
			return properties.get( property );
		else
			return "";
	}

	public void setProperty( int property, String value )
	{
		if ( ( property >= 0 ) && ( property < CONFIG_NLINES ) )
			properties.set( property, value );
	}

	public static String getMediaPath()
	{
		return mediaFolder;
	}

	public static void setMediaPath( String directory )
	{
		mediaFolder = directory;
	}

	public static boolean getColorWrapAround()
	{
		return wrapAroundPixelValues;
	}

	public static void setColorWrapAround( boolean bool )
	{
		wrapAroundPixelValues = bool;
	}

	public ArrayList<String> readConfig()
	{
		ArrayList<String> properties = null;
		try
		{
			String inputFileName =
			System.getProperty("user.home") +
			File.separatorChar + JES_CONFIG_FILE_NAME;
			File inputFile = new File(inputFileName);
			FileInputStream in = new
			FileInputStream(inputFile);

			byte bt[] = new
			byte[(int)inputFile.length()];
			in.read(bt);
			String s = new String(bt);
			in.close();
			properties = new ArrayList<String>(Arrays.asList(s.split("\r\n|\r|\n")));
			//you must be upgrading; adding blanks...
			while ( properties.size() < CONFIG_NLINES )
				properties.add("");
		}
		catch(java.io.IOException e)
		{
		        System.out.println( "Cannot access JESConfig file," + JES_CONFIG_FILE_NAME );
				  System.out.println(e);
		}
		return properties;
	}
}