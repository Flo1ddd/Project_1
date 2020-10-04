import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;


public class Test {
    public static void main(String[] args){
        System.out.println("Hello");
        System.setProperty("webdriver.edge.driver", "D:\\Test\\msedgedriver.exe");
        WebDriver dr = new EdgeDriver();
        dr.get("https://yandex.ru/");
        dr.findElement(By.className("desk-notif-card__login-mail-promo")).click();
        dr.findElement(By.name("firstname")).sendKeys("Ivan");
        dr.quit();
    }
}
