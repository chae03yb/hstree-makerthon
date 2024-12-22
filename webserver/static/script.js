let map; // 지도 객체
let markers = []; // 마커 객체를 저장하는 배열
let circles = []; // 원 객체를 저장하는 배열

// 지도 초기화
async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  const defaultPosition = { lat: 0, lng: 0 };

  map = new Map(document.getElementById("map"), {
    zoom: 2,
    center: defaultPosition,
    mapId: "DEMO_MAP_ID",
  });

  // JSON 파일에서 좌표를 로드하고 마커를 표시
  await loadCoordinates();
}

// JSON 파일에서 좌표를 로드
async function loadCoordinates() {
  try {
    const response = await fetch("coordinates.json");
    const data = await response.json();

    // 기존 마커와 원 제거
    clearOverlays();

    // 새로운 마커와 원 추가
    data.forEach((coord) => {
      addMarkerAndCircle(coord.lat, coord.lng, coord.title, coord.value, coord.event);
    });

    // 첫 번째 좌표로 지도 중심 이동
    if (data.length > 0) {
      const firstCoord = data[0];
      map.setCenter({ lat: firstCoord.lat, lng: firstCoord.lng });
    }
  } catch (error) {
    console.error("좌표 데이터를 불러오는 중 오류 발생:", error);
  }
}

// 지도에 마커와 원 추가
function addMarkerAndCircle(lat, lng, title, value, eventSize) {
  const position = { lat, lng };

  // 마커 아이콘 설정 (조건에 따라 다르게 적용)
  let iconUrl;
  let iconSize;
  if (value <= 50) {
    iconUrl = "images/marker1.png"; // 1번 마커
    iconSize = new google.maps.Size(40, 40);
  } else if (value <= 70) {
    iconUrl = "images/marker2.png"; // 2번 마커
    iconSize = new google.maps.Size(40, 40);
  } else {
    iconUrl = "images/marker3.png"; // 3번 마커
    iconSize = new google.maps.Size(60, 60);
  }

  const marker = new google.maps.Marker({
    map: map,
    position: position,
    title: title,
    icon: {
      url: iconUrl,
      scaledSize: iconSize, // 마커 크기 설정
    },
  });

  markers.push(marker);

  // 이벤트 크기에 따라 원 추가
  if (value > 50) {
    const radius = eventSize; // 반지름 설정 (eventSize 사용)
    const circle = new google.maps.Circle({
      map: map,
      center: position,
      radius: radius, // 반지름 (미터 단위)
      fillColor: "red", // 채우기 색상
      fillOpacity: 0.35, // 채우기 투명도
      strokeColor: "red", // 테두리 색상
      strokeOpacity: 0.8, // 테두리 투명도
      strokeWeight: 2, // 테두리 두께
    });

    circles.push(circle);
  }
}

// 기존 마커와 원 제거
function clearOverlays() {
  // 모든 마커 제거
  markers.forEach((marker) => marker.setMap(null));
  markers = [];

  // 모든 원 제거
  circles.forEach((circle) => circle.setMap(null));
  circles = [];
}

// 버튼 이벤트 처리
document.addEventListener("DOMContentLoaded", () => {
  initMap();
});
