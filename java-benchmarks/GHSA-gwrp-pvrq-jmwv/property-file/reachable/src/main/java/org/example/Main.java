package org.example;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Properties;

public class Main {
  public static void main(String[] args) {
    try {
      Properties properties = new Properties();
      properties.load(Thread.currentThread().getContextClassLoader().getResourceAsStream("app.properties"));
      Class<?> cls = Class.forName(properties.get("VulnerableClass").toString());
      Method m = cls.getDeclaredMethod("normalize", String.class);
      Object res = m.invoke(null, "I'm vulnerable!");
      System.out.println(res);
    } catch (IOException | ClassNotFoundException | NoSuchMethodException | IllegalAccessException |
             InvocationTargetException e) {
      throw new RuntimeException(e);
    }
  }
}