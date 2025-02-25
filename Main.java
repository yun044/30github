class SmartHomeDevice {
    protected String deviceName;
    protected boolean isOn;
    protected int powerLevel;
    protected String location;

    public SmartHomeDevice(String name, String loc) {
        this.deviceName = name;
        this.isOn = false;
        this.powerLevel = 0;
        this.location = loc;
    }

    public void turnOn() {
        isOn = true;
        System.out.println("\n[Действие] " + deviceName + " в локации '" + location + "' включено.");
    }

    public void turnOff() {
        isOn = false;
        System.out.println("\n[Действие] " + deviceName + " в локации '" + location + "' выключено.");
    }

    public void setPowerLevel(int level) {
        if (level < 0) level = 0;
        if (level > 100) level = 100;
        powerLevel = level;
        System.out.println("\n[Действие] " + deviceName + " в локации '" + location + "' установлен уровень мощности: " + powerLevel + "%.");
    }

    public void showStatus() {
        System.out.println("\n======= Статус устройства =======");
        System.out.println("Устройство: \t" + deviceName);
        System.out.println("Локация: \t" + location);
        System.out.println("Состояние: \t" + (isOn ? "Включено" : "Выключено"));
        System.out.println("Уровень мощности: \t" + powerLevel + "%");
        System.out.println("===============================\n");
    }

    public void moveToLocation(String newLocation) {
        location = newLocation;
        System.out.println("\n[Действие] " + deviceName + " перемещено в локацию '" + location + "'.");
    }
}


class SmartLamp extends SmartHomeDevice {
    private String color;

    public SmartLamp(String name, String loc) {
        super(name, loc);
        this.color = "Белый";
    }

    public void changeColor(String newColor) {
        this.color = newColor;
        System.out.println("\n[Действие] " + deviceName + " изменил цвет на: " + color);
    }

    @Override
    public void showStatus() {
        super.showStatus();
        System.out.println("Цвет: \t" + color);
        System.out.println("===============================\n");
    }
}


class SmartFridge extends SmartHomeDevice {
    private int temperature;
    private int items;

    public SmartFridge(String name, String loc) {
        super(name, loc);
        this.temperature = 4;
        this.items = 0;
    }

    public void setTemperature(int temp) {
        this.temperature = Math.max(-20, Math.min(temp, 10));
        System.out.println("\n[Действие] " + deviceName + " установлена температура: " + temperature + "°C.");
    }

    public void addItems(int quantity) {
        if (quantity > 0) {
            items += quantity;
            System.out.println("\n[Действие] " + deviceName + " добавлено продуктов: " + quantity + ". Теперь их: " + items);
        } else {
            System.out.println("\n[Ошибка] " + deviceName + " нельзя добавить отрицательное количество продуктов.");
        }
    }

    public void checkItems() {
        System.out.println("\n[Информация] " + deviceName + " в локации '" + location + "' содержит продуктов: " + items);
    }

    @Override
    public void showStatus() {
        super.showStatus();
        System.out.println("Температура: \t" + temperature + "°C");
        System.out.println("Количество продуктов: \t" + items);
        System.out.println("===============================\n");
    }
}


class SmartPet extends SmartHomeDevice {
    private int happinessLevel;
    private int hungerLevel;

    public SmartPet(String name, String loc) {
        super(name, loc);
        this.happinessLevel = 50;
        this.hungerLevel = 50;
    }

    public void feed() {
        if (hungerLevel > 0) {
            hungerLevel -= 20;
            if (hungerLevel < 0) hungerLevel = 0;
            System.out.println("\n[Действие] " + deviceName + " в локации '" + location + "' покормлен.");
            System.out.println("Текущий уровень голода: " + hungerLevel + "%\n");
        } else {
            System.out.println("\n[Предупреждение] " + deviceName + " не голоден!\n");
        }
    }

    public void play() {
        happinessLevel += 30;
        if (happinessLevel > 100) happinessLevel = 100;
        System.out.println("\n[Действие] " + deviceName + " в локации '" + location + "' поиграл.");
        System.out.println("Текущий уровень счастья: " + happinessLevel + "%\n");
    }

    @Override
    public void showStatus() {
        super.showStatus();
        System.out.println("Уровень счастья: \t" + happinessLevel + "%");
        System.out.println("Уровень голода: \t" + hungerLevel + "%");
        System.out.println("===============================\n");
    }
}


class SmartVehicle extends SmartHomeDevice {
    private int fuelLevel;
    private int speed;

    public SmartVehicle(String name, String loc) {
        super(name, loc);
        this.fuelLevel = 100;
        this.speed = 0;
    }

    public void accelerate(int increment) {
        speed += increment;
        if (speed > 220) speed = 220;
        System.out.println("\n[Действие] " + deviceName + " в локации '" + location + "' ускорился.");
        System.out.println("Текущая скорость: " + speed + " км/ч\n");
    }

    public void refuel(int amount) {
        fuelLevel += amount;
        if (fuelLevel > 100) fuelLevel = 100;
        System.out.println("\n[Действие] " + deviceName + " в локации '" + location + "' заправлен.");
        System.out.println("Текущий уровень топлива: " + fuelLevel + "%\n");
    }

    @Override
    public void showStatus() {
        super.showStatus();
        System.out.println("Уровень топлива: \t" + fuelLevel + "%");
        System.out.println("Текущая скорость: \t" + speed + " км/ч");
        System.out.println("===============================\n");
    }
}


public class Main {
    public static void main(String[] args) {
        SmartHomeDevice cleaner = new SmartHomeDevice("Пылесос", "Гостиная");
        cleaner.turnOn();
        cleaner.setPowerLevel(75);
        cleaner.showStatus();
        cleaner.moveToLocation("Спальня");
        cleaner.setPowerLevel(15);
        cleaner.turnOff();
        cleaner.showStatus();

        SmartLamp lamp = new SmartLamp("Лампа", "Кухня");
        lamp.turnOn();
        lamp.changeColor("Синий");
        lamp.showStatus();

        SmartFridge fridge = new SmartFridge("Холодильник", "Кухня");
        fridge.turnOn();
        fridge.setTemperature(3);
        fridge.addItems(5);
        fridge.addItems(3);
        fridge.checkItems();
        fridge.moveToLocation("Гостиная");
        fridge.turnOff();
        fridge.showStatus();

        SmartPet pet = new SmartPet("Рекс", "Улица");
        pet.turnOn();
        pet.feed();
        pet.play();
        pet.showStatus();
        pet.moveToLocation("Дом");
        pet.turnOff();
        pet.showStatus();

        SmartVehicle car = new SmartVehicle("Tesla", "Парковка");
        car.turnOn();
        car.accelerate(100);
        car.refuel(30);
        car.showStatus();
        car.moveToLocation("Трасса");
        car.showStatus();
    }
}





