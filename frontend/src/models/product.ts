export enum Category {
  Saddle = 'Saddle',
  Stirrups = 'Stirrups',
  Accessory = 'Accessory',
}

export interface Product {
  id?: number
  name: string
  stock: number
  price: number
  category: Category | null
}
