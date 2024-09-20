package org.example;

import org.apache.commons.io.FilenameUtils;
import java.util.stream.Stream;

public class Main {
  public static void main(String[] args) {
    Stream.of("Hello world!").map(FilenameUtils::normalize).forEach(System.out::println);
  }
}