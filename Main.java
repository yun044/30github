class SmartHomeDevice {
    private String deviceName;
    private boolean isOn;
    private int powerLevel;
    private String location;

    public SmartHomeDevice(String name, String loc) {
        this.deviceName = name;
        this.isOn = false;
        this.powerLevel = 0;
        this.location = loc;
    }

    public String getDeviceName() {
        return deviceName;
    }

    public void setDeviceName(String deviceName) {
        this.deviceName = deviceName;
    }

    public boolean isOn() {
        return isOn;
    }

    public void setOn(boolean on) {
        isOn = on;
    }

    public int getPowerLevel() {
        return powerLevel;
    }

    public void setPowerLevel(int powerLevel) {
        if (powerLevel < 0) powerLevel = 0;
        if (powerLevel > 100) powerLevel = 100;
        this.powerLevel = powerLevel;
        System.out.println("\n[Действие] " + getDeviceName() + " в локации '" + getLocation() + "' установлен уровень мощности: " + powerLevel + "%.");
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
        System.out.println("\n[Действие] " + getDeviceName() + " перемещено в локацию '" + location + "'.");
    }

    public void turnOn() {
        if (!isOn()) {
            setOn(true);
            System.out.println("\n[Действие] " + getDeviceName() + " в локации '" + getLocation() + "' включено.");
        } else {
            System.out.println("\n[Предупреждение] " + getDeviceName() + " уже включено.");
        }
    }

    public void turnOff() {
        if (isOn()) {
            setOn(false);
            System.out.println("\n[Действие] " + getDeviceName() + " в локации '" + getLocation() + "' выключено.");
        } else {
            System.out.println("\n[Предупреждение] " + getDeviceName() + " уже выключено.");
        }
    }

    public void showStatus() {
        System.out.println("\n======= Статус устройства =======");
        System.out.println("Устройство: \t" + getDeviceName());
        System.out.println("Локация: \t" + getLocation());
        System.out.println("Состояние: \t" + (isOn() ? "Включено" : "Выключено"));
        System.out.println("Уровень мощности: \t" + getPowerLevel() + "%");
        System.out.println("===============================\n");
    }

    public void moveToLocation(String newLocation) {
        setLocation(newLocation);
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
        System.out.println("\n[Действие] " + getDeviceName() + " изменил цвет на: " + color);
    }

    public void changeColor(String newColor, int brightness) {
        this.color = newColor;
        setPowerLevel(brightness);
        System.out.println("\n[Действие] " + getDeviceName() + " изменил цвет на: " + color + " с яркостью: " + brightness + "%");
    }

    @Override
    public void turnOn() {
        super.turnOn();
        setPowerLevel(50);
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

    @Override
    public void turnOn() {
        super.turnOn();
        setTemperature(4);
    }

    public void setTemperature(int temp) {
        this.temperature = Math.max(-20, Math.min(temp, 10));
        System.out.println("\n[Действие] " + getDeviceName() + " установлена температура: " + temperature + "°C.");
    }

    public void addItems(int quantity) {
        if (quantity > 0) {
            items += quantity;
            System.out.println("\n[Действие] " + getDeviceName() + " добавлено продуктов: " + quantity + ". Теперь их: " + items);
        } else {
            System.out.println("\n[Ошибка] " + getDeviceName() + " нельзя добавить отрицательное количество продуктов.");
        }
    }

    public void checkItems() {
        System.out.println("\n[Информация] " + getDeviceName() + " в локации '" + getLocation() + "' содержит продуктов: " + items);
    }

    @Override
    public void showStatus() {
        super.showStatus();
        System.out.println("Температура: \t" + temperature + "°C");
        System.out.println("Количество продуктов: \t" + items);
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

    public int getFuelLevel() {
        return fuelLevel;
    }

    private void setFuelLevel(int fuelLevel) {
        this.fuelLevel = Math.max(0, Math.min(fuelLevel, 100));
    }

    public int getSpeed() {
        return speed;
    }

    private void setSpeed(int speed) {
        this.speed = Math.max(0, Math.min(speed, 220));
    }

    public void accelerate(int increment) {
        accelerate(increment, 5);
    }

    public void accelerate(int increment, int fuelConsumption) {
        if (fuelLevel > 0) {
            setSpeed(speed + increment);
            setFuelLevel(fuelLevel - fuelConsumption);
            System.out.println("\n[Действие] " + getDeviceName() + " ускорился до " + speed + " км/ч.");
            System.out.println("[Топливо] Уровень топлива: " + fuelLevel + "% (потрачено " + fuelConsumption + "%).");
        } else {
            System.out.println("\n[Ошибка] " + getDeviceName() + " закончилось топливо!");
        }
    }

    public void refuel(int amount) {
        setFuelLevel(fuelLevel + amount);
        System.out.println("\n[Действие] " + getDeviceName() + " заправлен. Уровень топлива: " + fuelLevel + "%.");
    }

    @Override
    public void turnOn() {
        if (fuelLevel > 0) {
            super.turnOn();
            setSpeed(0);
        } else {
            System.out.println("\n[Ошибка] " + getDeviceName() + " не может включиться, так как нет топлива!");
        }
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
        SmartLamp lamp = new SmartLamp("Лампа", "Кухня");
        lamp.turnOn();
        lamp.changeColor("Синий");
        lamp.changeColor("Красный", 80);
        lamp.setPowerLevel(80);
        lamp.showStatus();

        SmartFridge fridge = new SmartFridge("Холодильник", "Подвал");
        fridge.turnOn();
        fridge.setTemperature(3);
        fridge.addItems(5);
        fridge.moveToLocation("Кухня");
        fridge.showStatus();

        SmartVehicle car = new SmartVehicle("BMW", "Парковка");
        car.setDeviceName("Mercedes");
        car.turnOn();
        car.accelerate(100);
        car.accelerate(50, 10);
        car.refuel(30);
        car.showStatus();
    }
}
