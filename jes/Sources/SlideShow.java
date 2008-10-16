public class SlideShow
{
  /////////// fields ///////////////
  public Picture[] pictureArray;
  private int waitTime;
  private String title;
  
  ///////////// constructors //////////
  
  public SlideShow() {}
  
  public SlideShow(Picture[] pictArray)
  {
    this.pictureArray = pictArray;
  }
  
  public SlideShow(Picture[] pictArray,
                   int time)
  {
    this.pictureArray = pictArray;
    this.waitTime = time;
  }
  
  //////////// methods ///////////////
  
  public String getTitle() { return this.title;}
  
  public void setTitle(String theTitle)
  {
    this.title = theTitle;
  }
  
  public int getWaitTime()
  { 
    return this.waitTime;
  }
  
  public Picture getPicture(int index)
  {
    if (this.pictureArray == null)
      return null;
    if (index < 0 || 
        index >= this.pictureArray.length)
      return null;
    return this.pictureArray[index];
  }

  public String toString()
  {
    String result = "A slide show with ";
    if (this.pictureArray != null)
      result = result + this.pictureArray.length +
       " pictures and ";
    else
      result = result + "no pictures and ";
    result = result + 
      "a wait time of " + this.waitTime;
    return result;
  }
  
  private void showTitle() throws Exception
  {
    Picture titlePict = new Picture(640,480);
    titlePict.addMessage(this.title, 100,100);
    titlePict.show();
    Thread.sleep(this.waitTime);
    titlePict.hide();
  }
  
  public void show() throws Exception
  {
    if (pictureArray != null)
    {
      // show the title as a slide
      Picture titlePict = new Picture(640,480);
      titlePict.addMessage(this.title,100,100);
      titlePict.show();
      Thread.sleep(this.waitTime);
      titlePict.hide();
      
      for (Picture currPict : pictureArray)
      {
        if (currPict != null)
        {
          currPict.show();
          Thread.sleep(waitTime);
          currPict.hide();
        }
      }
    }
  }
  
  public static void main(String[] args) throws Exception
  {
    Picture[] pictArray = new Picture[5];
    pictArray[0] = new Picture(FileChooser.getMediaPath("beach.jpg"));
    pictArray[1] = new Picture(FileChooser.getMediaPath("blueShrub.jpg"));
    pictArray[2] = new Picture(FileChooser.getMediaPath("church.jpg"));
    pictArray[3] = new Picture(FileChooser.getMediaPath("redDoor.jpg"));
    pictArray[4] = new Picture(FileChooser.getMediaPath("butterfly.jpg"));
    SlideShow show1 = new SlideShow(pictArray,1000);
    show1.setTitle("Vacation Slides");
    show1.show();
  }
}